"use client";

import Link from "next/link";
import { Geist, Geist_Mono } from "next/font/google";
import { useState, useEffect, useContext } from "react";
import { Bell } from "lucide-react";
import { AuthContext, AuthProvider } from "./context/AuthContext"; // Import Auth Context
import "./globals.css";

interface Notification {
  id: number;
  message: string;
  is_read: boolean;
  created_at: string;
}

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <AuthProvider>
      <LayoutContent>{children}</LayoutContent>
    </AuthProvider>
  );
}

function LayoutContent({ children }: { children: React.ReactNode }) {
  const { user, logout } = useContext(AuthContext);
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [showNotifications, setShowNotifications] = useState(false);
  //const [user, setUser] = useState<{ username: string } | null>(null);

  // Fetch notifications
  useEffect(() => {
    const fetchNotifications = async () => {
      const token = localStorage.getItem("access_token");
      if (!token) return;

      try {
        const res = await fetch("http://127.0.0.1:8000/api/notifications/", {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (!res.ok) {
          console.log("Failed to fetch notifications");
          return;
        }

        const data = await res.json();
        setNotifications(data);
      } catch (err) {
        console.error("Notifications Error:", err);
      }
    };

    fetchNotifications();
  }, []);


  return (
    <html lang="en">
      <body className="bg-gray-100 dark:bg-gray-800 text-black dark:text-white antialiased">
        {/* Navbar */}
        <nav className="flex justify-between items-center p-4 bg-white shadow-md">
          <Link href="/" className="text-2xl font-bold text-blue-600">
            eLearnHub
          </Link>
          <div className="space-x-6 flex items-center">
            <Link href="/courses" className="text-gray-700 hover:text-blue-600">
              Courses
            </Link>

            {/* Notification Bell */}
            <div className="relative cursor-pointer" onClick={() => setShowNotifications(!showNotifications)}>
              <Bell className="w-6 h-6 text-gray-700 hover:text-blue-600" />
              {notifications.length > 0 && (
                <span className="absolute top-0 right-0 bg-red-600 text-white text-xs w-4 h-4 rounded-full flex items-center justify-center">
                  {notifications.length}
                </span>
              )}
            </div>

            {/* Notifications Modal */}
            {showNotifications && (
              <div className="absolute top-16 right-4 bg-white shadow-lg p-4 w-64 rounded-lg z-50">
                <h3 className="font-bold">Notifications</h3>
                {notifications.length > 0 ? (
                  <ul>
                    {notifications.map((notif) => (
                      <li key={notif.id} className="text-gray-700 border-b py-2">
                        {notif.message}
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p className="text-gray-500">No new notifications</p>
                )}
                <button
                  onClick={() => setShowNotifications(false)}
                  className="mt-2 text-blue-600 underline"
                >
                  Close
                </button>
              </div>
            )}

            {/* Conditional Rendering for Auth */}
            {!user ? (
              <>
                <Link href="/login" className="text-gray-700 hover:text-blue-600">
                  Login
                </Link>
                <Link href="/register" className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
                  Sign Up
                </Link>
              </>
            ) : (
              <div className="flex items-center space-x-4">
              <Link href="/dashboard" className="flex items-center justify-center w-12 h-10 bg-gray-300 rounded-full">
              {user?.username?.[0]?.toUpperCase() || ""}
              </Link>
              <button onClick={logout} className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700">
                Logout
              </button>
            </div>
            )}
          </div>
        </nav>


        {/* Page Content */}
        <main className="p-6">{children}</main>

        {/* Footer */}
        <footer className="bg-gray-200 dark:bg-gray-900 text-center p-4 mt-auto">
          &copy; {new Date().getFullYear()} eLearnHub - All Rights Reserved
        </footer>
      </body>
    </html>
  );
}