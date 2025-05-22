"use client";
import { useEffect, useState } from "react";

interface Notification {
  id: number;
  message: string;
  is_read: boolean;
  created_at: string;
}

export default function Notifications() {
  const [notifications, setNotifications] = useState<Notification[]>([]);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) return;

    fetch("http://127.0.0.1:8000/api/notifications/", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("Fetched Notifications:", data); // Debugging
        setNotifications(Array.isArray(data) ? data : []);
      })
      .catch((err) => console.error("Error fetching notifications:", err));
  }, []);

  return (
    <div className="p-4 bg-white dark:bg-gray-700 rounded-lg shadow mb-6">
      {notifications.length === 0 ? (
        <p className="text-gray-500">No notifications yet.</p>
      ) : (
        <ul>
          {notifications.map((notif) => (
            <li key={notif.id} className="border-b p-2">
              <p className="text-gray-700">{notif.message}</p>
              <p className="text-xs text-gray-500">{new Date(notif.created_at).toLocaleString()}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}