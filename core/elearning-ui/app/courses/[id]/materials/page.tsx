"use client";
import { useEffect, useState } from "react";
import { useRouter, useParams } from "next/navigation";

interface Material {
  id: number;
  title: string;
  description: string;
  file_url: string;
  file_type: string;
}

interface Section {
  id: number;
  title: string;
}

export default function CourseMaterials() {
  const { id: rawId } = useParams(); // Course ID from URL
  const courseId = parseInt(rawId as string, 10);
  const router = useRouter();

  const [userRole, setUserRole] = useState<string | null>(null);
  const [materials, setMaterials] = useState<Material[]>([]);
  const [sections, setSections] = useState<Section[]>([]);
  const [selectedSection, setSelectedSection] = useState<number | null>(null);
  const [newSectionTitle, setNewSectionTitle] = useState("");
  const [newMaterial, setNewMaterial] = useState<{ title: string; description: string; file: File | null }>({
    title: "",
    description: "",
    file: null,
  });

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      router.push("/login");
      return;
    }

    const fetchUser = async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/profile/?include_courses=true", {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (!res.ok) throw new Error("Failed to fetch user profile");

        const data = await res.json();
        console.log("Full Profile API Response:", data);

        setUserRole(data.role || "student"); // Default to student

        // Fetch sections if user role is valid
        if (courseId) {
          fetchSections(token);
        }
      } catch (error) {
        console.error("Error fetching user profile:", error);
        setUserRole("student"); // Fallback
      }
    };

    fetchUser();
  }, [courseId]);

  const fetchSections = async (token: string) => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/courses/${courseId}/sections/`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!res.ok) throw new Error("Failed to fetch sections");

      const data = await res.json();
      console.log("Fetched Sections:", data);

      setSections(data);
      if (data.length > 0) {
        setSelectedSection(data[0].id);
        fetchMaterials(data[0].id, token);
      }
    } catch (error) {
      console.error("Error fetching sections:", error);
    }
  };

  const fetchMaterials = async (sectionId: number, token: string) => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/sections/${sectionId}/materials/`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!res.ok) throw new Error("Failed to fetch materials");

      const data = await res.json();
      console.log("Fetched Materials:", data);
      setMaterials(data);
    } catch (error) {
      console.error("Error fetching materials:", error);
    }
  };

  const handleCreateSection = async () => {
    if (!newSectionTitle.trim()) return alert("Section title cannot be empty.");
    const token = localStorage.getItem("access_token");

    try {
      const res = await fetch(`http://127.0.0.1:8000/api/courses/${courseId}/sections/`, {
        method: "POST",
        headers: { 
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}` 
        },
        body: JSON.stringify({ title: newSectionTitle, structure_type: "custom" }),
      });

      const data = await res.json();
      if (res.ok) {
        setSections((prev) => [...prev, data]); 
        setNewSectionTitle("");
      } else {
        console.error("Section creation failed:", data);
        alert("Failed to create section: " + JSON.stringify(data));
      }
    } catch (error) {
      console.error("Error creating section:", error);
    }
  };

  const handleUpload = async (e: any) => {
    e.preventDefault();
    const token = localStorage.getItem("access_token");

    if (!selectedSection) {
      alert("Please select a section before uploading.");
      return;
    }

    const formData = new FormData();
    formData.append("title", newMaterial.title);
    formData.append("description", newMaterial.description);
    formData.append("file", newMaterial.file as Blob);

    try {
      const res = await fetch(`http://127.0.0.1:8000/api/sections/${selectedSection}/materials/`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },  
        body: formData,
      });

      if (res.ok) {
        const material = await res.json();
        setMaterials((prev) => [...prev, material]);  
        setNewMaterial({ title: "", description: "", file: null });
      } else {
        alert("Upload failed.");
      }
    } catch (error) {
      console.error("Error uploading material:", error);
    }
  };

  const handleDelete = async (materialId: number) => {
    if (!confirm("Are you sure you want to delete this material?")) return;
    const token = localStorage.getItem("access_token");

    try {
      await fetch(`http://127.0.0.1:8000/api/materials/${materialId}/delete/`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
      });

      setMaterials((prev) => prev.filter((m) => m.id !== materialId));
    } catch (error) {
      console.error("Error deleting material:", error);
    }
  };

  return (
    <div className="p-6 min-h-screen bg-gray-100 dark:bg-gray-800">
      <h1 className="text-3xl font-bold mb-6">Course Materials</h1>

      {/* SECTION CREATION (for Teachers) */}
      {userRole === "teacher" && (
        <div className="mb-6 bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-bold mb-2">Create a New Section</h2>
          <input
            type="text"
            placeholder="Enter section title..."
            className="border p-2 w-full mb-2 rounded"
            value={newSectionTitle}
            onChange={(e) => setNewSectionTitle(e.target.value)}
          />
          <button onClick={handleCreateSection} className="bg-green-600 text-white px-4 py-2 rounded">
            Create Section
          </button>
        </div>
      )}

      {/* SECTIONS LIST */}
      {sections.length > 0 ? (
        <div className="mb-6">
          <h2 className="text-xl font-bold mb-2">Sections</h2>
          <ul className="border p-4 rounded bg-white shadow">
            {sections.map((section) => (
              <li
                key={section.id}
                className={`p-2 cursor-pointer text-black ${
                  selectedSection === section.id ? "bg-yellow-700" : "hover:bg-gray-200"
                }`}
                onClick={() => {
                  setSelectedSection(section.id);
                  fetchMaterials(section.id, localStorage.getItem("access_token") || "");
                }}
              >
                {section.title}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p className="text-gray-500">No sections created yet.</p>
      )}

      {/* MATERIAL UPLOAD FORM (Only for Teachers) */}
      {userRole === "teacher" && selectedSection && (
        <form onSubmit={handleUpload} className="bg-white p-6 rounded-lg shadow mb-6">
          <h2 className="text-2xl font-bold mb-4">Upload New Material</h2>
          <input
            type="text"
            placeholder="Title"
            className="border p-2 w-full mb-2 rounded"
            value={newMaterial.title}
            onChange={(e) => setNewMaterial({ ...newMaterial, title: e.target.value })}
          />
          <input type="file" className="border p-2 w-full mb-2" onChange={(e) => setNewMaterial({ ...newMaterial, file: e.target.files ? e.target.files[0] : null })}/>
          <button type="submit" className="bg-blue-600 text-white p-2 rounded hover:bg-blue-700">Upload</button>
        </form>
      )}

      {/* DISPLAY COURSE MATERIALS */}
      {materials.length > 0 ? (
        <div className="text-black grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {materials.map((material) => (
            <div key={material.id} className="bg-white shadow-md rounded-lg p-4">
              <h3 className="text-lg font-bold">{material.title}</h3>
              <p className="text-gray-500">{material.description}</p>
              <a href={material.file_url} target="_blank" className="text-blue-600 hover:underline">
                View Material
              </a>
            </div>
          ))}
        </div>
      ) : (
        <p className="text-gray-500 mt-4">No materials uploaded yet.</p>
      )}
    </div>
  );
}