"use client";
import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";

export default function Enroll() {
  const { id } = useParams();
  const router = useRouter();
  const [enrolled, setEnrolled] = useState(false);

  const refreshToken = async () => {
    const refresh = localStorage.getItem("refresh_token");
    if (!refresh) {
      console.log("No refresh token found");
      return null;
    }
  
    const res = await fetch("http://127.0.0.1:8000/api/token/refresh/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh }),
    });
  
    if (!res.ok) {
      console.log("Token refresh failed");
      return null;
    }
  
    const data = await res.json();
    localStorage.setItem("access_token", data.access);
    return data.access;
  };
  
  const handleEnroll = async () => {
    let token = localStorage.getItem("access_token");
  
    const res = await fetch(`http://127.0.0.1:8000/api/courses/${id}/enroll/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    });
  
    if (res.status === 401) {
      console.log("Token expired, refreshing...");
      token = await refreshToken();
      if (!token) {
        alert("Session expired. Please log in again.");
        return;
      }
  
      const retryRes = await fetch(`http://127.0.0.1:8000/api/courses/${id}/enroll/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      });
  
      if (retryRes.ok) {
        setEnrolled(true);
      } else {
        alert("Enrollment failed");
      }
    } else if (res.ok) {
      setEnrolled(true);
    } else {
      alert("Enrollment failed");
    }
  };

  return (
    <div className="p-6 min-h-screen bg-gray-100 dark:bg-gray-800 text-center">
      <h1 className="text-3xl font-bold mb-4">Enroll in Course</h1>
      {enrolled ? (
        <p className="text-green-600 text-xl">✅ Successfully Enrolled!</p>
      ) : (
        <button onClick={handleEnroll} className="bg-blue-600 text-white p-2 rounded hover:bg-blue-700">
          Enroll Now
        </button>
      )}
    </div>
  );
}