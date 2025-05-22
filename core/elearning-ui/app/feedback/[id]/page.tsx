"use client";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";

interface Feedback {
  student: string;
  rating: number;
  comment: string;
}

export default function FeedbackPage() {
  const { id } = useParams();
  const [feedback, setFeedback] = useState<Feedback[]>([]);
  const [newFeedback, setNewFeedback] = useState({ rating: 5, comment: "" });

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      console.error("No token found, authentication required.");
      return;
    }

    fetch(`http://127.0.0.1:8000/api/feedback/?course=${id}`, {
    headers: { Authorization: `Bearer ${token}` }, // Include token
  })
    .then((res) => {
      if (!res.ok) {
        throw new Error("Failed to fetch feedback");
      }
      return res.json();
    })
      .then((data) => {
        // Ensure data is an array before setting state
        setFeedback(Array.isArray(data) ? data : []);
      })
      .catch((err) => {
        console.error("Error fetching feedback:", err);
        setFeedback([]); // Fallback to empty array
      });
  }, [id]);

  const handleSubmit = async () => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      console.error("No token found, authentication required.");
      return;
    }
  
    const feedbackData = {
      course: id, // Ensure course ID is sent
      rating: newFeedback.rating,
      comment: newFeedback.comment,
    };
  
    console.log("Submitting Feedback:", feedbackData); // Debugging
  
    try {
      const res = await fetch("http://127.0.0.1:8000/api/feedback/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(feedbackData),
      });
  
      const responseData = await res.json();
  
      if (!res.ok) {
        console.error("Feedback submission failed:", responseData); // Log error details
        return;
      }
  
      console.log("Feedback submitted successfully:", responseData);
  
      setNewFeedback({ rating: 5, comment: "" });
  
      // Refresh feedback list
      fetch(`http://127.0.0.1:8000/api/feedback/?course=${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      })
        .then((res) => res.json())
        .then((data) => {
          setFeedback(Array.isArray(data) ? data : []);
        })
        .catch((err) => console.error("Error fetching feedback:", err));
  
    } catch (error) {
      console.error("Error submitting feedback:", error);
    }
  };

  return (
    <div className="p-6 min-h-screen ">
      <h1 className="text-3xl font-bold mb-4">Course Feedback</h1>

      {/* Ensure feedback is an array before mapping */}
      {feedback.length === 0 ? (
        <p className="text-gray-600">No feedback yet.</p>
      ) : (
        <ul className="mb-6 text-gray-600">
          {feedback.map((item, index) => (
            <li key={index} className="border p-3 my-2 rounded bg-white">
              <p className="font-bold">{item.student}</p>
              <p>⭐ {item.rating}/5</p>
              <p>{item.comment}</p>
            </li>
          ))}
        </ul>
      )}

      <h2 className="text-2xl font-bold mb-2">Leave Feedback</h2>

      {/* Rating Selection */}
      <label className="block text-gray-700 dark:text-gray-200 font-semibold">Rating:</label>
      <select className="border p-2 rounded text-black w-full" value={newFeedback.rating}
        onChange={(e) => setNewFeedback({ ...newFeedback, rating: Number(e.target.value) })}>
        {[1, 2, 3, 4, 5].map((num) => ( <option key={num} value={num}> {num} ⭐
          </option>
        ))}
      </select>

      {/* Comment Input */}
      <label className="block text-gray-700 dark:text-gray-200  font-semibold mt-4">Comment:</label>
      <textarea
        className="w-full border p-2 rounded text-black"
        value={newFeedback.comment}
        onChange={(e) => setNewFeedback({ ...newFeedback, comment: e.target.value })}
      />

      {/* Submit Button */}
      <button
        onClick={handleSubmit}
        className="bg-blue-600 text-white p-2 rounded hover:bg-blue-700 mt-2"
      >
        Submit Feedback
      </button>
    </div>
  );
}