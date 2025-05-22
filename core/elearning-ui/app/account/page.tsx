"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

export default function Account() {
  const [user, setUser] = useState({ username: "", email: "", profile_picture: "" });
  const [newUsername, setNewUsername] = useState("");
  const [newEmail, setNewEmail] = useState("");
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [profilePicture, setProfilePicture] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      router.push("/login");
      return;
    }

    fetch("http://127.0.0.1:8000/api/profile/", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => {
        setUser(data);
        setNewUsername(data.username);
        setNewEmail(data.email);
      });
  }, []);

  // Handle profile update
  const handleProfileUpdate = async () => {
    const token = localStorage.getItem("access_token");
    const response = await fetch("http://127.0.0.1:8000/api/update_profile/", {
      method: "PUT",
      headers: { 
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify({ username: newUsername, email: newEmail, password: newPassword }),
    });

    if (response.ok) {
      alert("Profile updated successfully!");
      window.location.reload();
    } else {
      alert("Failed to update profile.");
    }
  };

  // Handle profile picture selection
  const handleProfilePictureChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setProfilePicture(file);

      // Preview image before uploading
      const reader = new FileReader();
      reader.onload = () => setPreview(reader.result as string);
      reader.readAsDataURL(file);
    }
  };

  // Handle profile picture upload
  const handleProfilePictureUpload = async () => {
    if (!profilePicture) return alert("Please select a file");

    const token = localStorage.getItem("access_token");
    const formData = new FormData();
    formData.append("profile_picture", profilePicture);

    const response = await fetch("http://127.0.0.1:8000/api/account/upload-profile-picture/", {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });
  
    if (response.ok) {
      alert("Profile picture updated successfully!");
      window.location.reload();
    } else {
      alert("Failed to update profile picture.");
    }
  };

  return (
    <div className="p-6 min-h-screen bg-gray-100 dark:bg-gray-800">
      <h1 className="text-3xl font-bold">Account Settings</h1>

      {/* Profile Picture Upload */}
      <div className="mt-6">
        <h2 className="text-xl font-bold">Profile Picture</h2>
        {preview && <img src={preview} alt="Preview" className="w-24 h-24 rounded-full mb-4" />}
        <input type="file" onChange={handleProfilePictureChange} className="block w-full p-2 border rounded mt-2" />
        <button onClick={handleProfilePictureUpload} className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700 mt-2">
          Upload & Crop
        </button>
      </div>

      {/* User Info */}
      <div className="mt-6">
        <h2 className="text-xl font-bold">Update Information</h2>
        <input type="text" className="w-full p-2 border rounded" value={newUsername} onChange={(e) => setNewUsername(e.target.value)} />
        <input type="email" className="w-full p-2 border rounded mt-2" value={newEmail} onChange={(e) => setNewEmail(e.target.value)} />
        <input type="password" className="w-full p-2 border rounded mt-2" placeholder="New Password" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} />
        <button onClick={handleProfileUpdate} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 mt-2">
          Save Changes
        </button>
      </div>
    </div>
  );
}