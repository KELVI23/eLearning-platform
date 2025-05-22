"use client";

import { useState, useEffect } from "react";
import { useRouter, useParams } from "next/navigation";

export default function CourseAction() {
  const router = useRouter();
  const { id } = useParams(); // Course ID (for enrolling)
  const [userRole, setUserRole] = useState<string | null>(null);
  const [courseData, setCourseData] = useState({
    title: "",
    description: "",
    image_url: "",
    difficulty_level: "Beginner",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Fetch user role
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
        console.log("User Profile API Response:", data);

        setUserRole(data.role || "student"); // Default to student

      } catch (error) {
        console.error("Error fetching user profile:", error);
        router.push("/login");
      }
    };

    fetchUser();
  }, [router]);

  // Handle form input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setCourseData({ ...courseData, [e.target.name]: e.target.value });
  };

  // Handle form submission for both creating and enrolling
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    const token = localStorage.getItem("access_token");
    try {
      let res;
      let data;

      if (userRole === "teacher") {
        // Create a course
        res = await fetch("http://127.0.0.1:8000/api/courses/create_course/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify(courseData),
        });
      } else {
        // Enroll in a course (for students)
        res = await fetch(`http://127.0.0.1:8000/api/courses/${id}/enroll/`, {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
      }

      data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || "Action failed.");
      }

      router.push("/courses"); // Redirect to courses list
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 min-h-screen text-black">
      <h1 className="text-3xl font-bold mb-6 dark:text-white">
        {userRole === "teacher" ? "Create a New Course" : "Enroll in Course"}
      </h1>

      {error && <p className="text-red-600 mb-4">{error}</p>}

      {userRole === "teacher" ? (
        <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md">
          <div className="mb-4">
            <label className="block text-sm font-medium">Title</label>
            <input
              type="text"
              name="title"
              value={courseData.title}
              onChange={handleChange}
              className="w-full p-2 border rounded"
              required
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium">Description</label>
            <textarea
              name="description"
              value={courseData.description}
              onChange={handleChange}
              className="w-full p-2 border rounded"
              required
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium">Image URL</label>
            <input
              type="text"
              name="image_url"
              value={courseData.image_url}
              onChange={handleChange}
              className="w-full p-2 border rounded"
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium">Difficulty Level</label>
            <select
              name="difficulty_level"
              value={courseData.difficulty_level}
              onChange={handleChange}
              className="w-full p-2 border rounded"
            >
              <option>Beginner</option>
              <option>Intermediate</option>
              <option>Advanced</option>
            </select>
          </div>

          <button
            type="submit"
            className={`w-full p-2 text-white bg-blue-600 rounded ${
              loading ? "opacity-50 cursor-not-allowed" : "hover:bg-blue-700"
            }`}
            disabled={loading}
          >
            {loading ? "Creating..." : "Create Course"}
          </button>
        </form>
      ) : (
        <button
          onClick={handleSubmit}
          className={`w-full p-2 text-white bg-green-600 rounded ${
            loading ? "opacity-50 cursor-not-allowed" : "hover:bg-green-700"
          }`}
          disabled={loading}
        >
          {loading ? "Enrolling..." : "Enroll in Course"}
        </button>
      )}
    </div>
  );
}