"use client";
import { useEffect, useState } from "react";

interface Status {
  user: string;
  content: string;
  created_at: string;
}

export default function StatusUpdates() {
  const [statuses, setStatuses] = useState<Status[]>([]);
  const [newStatus, setNewStatus] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      console.warn("No token found, user is not authenticated.");
      return;
    }

    fetch("http://127.0.0.1:8000/api/statuses/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch statuses: Unauthorized");
        }
        return res.json();
      })
      .then((data) => {
        console.log("Fetched Status Updates:", data);
        setStatuses(Array.isArray(data) ? data : []);
      })
      .catch((err) => {
        console.error("Error fetching statuses:", err);
        setStatuses([]); // Prevent breaking `.map()`
      });
  }, []);

  const handlePostStatus = async () => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      alert("You must be logged in to post a status.");
      return;
    }
  
    if (!newStatus.trim()) {
      alert("Status content cannot be empty.");
      return;
    }
  
    try {
      const response = await fetch("http://127.0.0.1:8000/api/statuses/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ content: newStatus.trim() }), 
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        console.error("Failed to post status:", errorData);
        alert(errorData.detail || "Failed to post status.");
        return;
      }
  
      const newStatusData = await response.json();
      setStatuses((prevStatuses) => [newStatusData, ...prevStatuses]);
      setNewStatus("");
    } catch (error) {
      console.error("Error posting status:", error);
      alert("Something went wrong while posting your status.");
    }
  };

  return (
    <div className="p-6 min-h-screen bg-gray-300 dark:bg-gray-800 text-black dark:text-white">
      <h1 className="text-3xl font-bold mb-4">Status Updates</h1>

      {statuses.length === 0 ? (
        <p className="text-gray-500 dark:text-gray-100">No statuses available.</p>
      ) : (
        <ul className="mb-6">
          {statuses.map((status, index) => (
            <li key={index} className="border p-3 my-2 rounded bg-white dark:bg-gray-700">
              <p className="font-bold">{status.user}</p>
              <p>{status.content}</p>
            </li>
          ))}
        </ul>
      )}

      <textarea
        className="w-full border p-2 rounded dark:text-black"
        value={newStatus}
        onChange={(e) => setNewStatus(e.target.value)}
        placeholder="What's on your mind?"
      />
      <button
        onClick={handlePostStatus}
        className="bg-blue-600 text-white p-2 rounded hover:bg-blue-700 mt-2"
      >
        Post Status
      </button>
    </div>
  );
}