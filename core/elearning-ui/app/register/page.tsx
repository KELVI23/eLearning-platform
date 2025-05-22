"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "", role: "student" });
  const router = useRouter();

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch("http://127.0.0.1:8000/api/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    if (res.ok) {
      router.push("/login");
    } else {
      alert("Registration failed");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen dark:bg-gray-500 bg-gray-100">
      <form onSubmit={handleRegister} className="bg-white dark:bg-gray-800 p-6 rounded shadow-md w-96 text-black">
        <h2 className="text-2xl font-bold mb-4 text-center text-white">Register</h2>
        <input type="text" placeholder="Username" className="border p-2 w-full mb-2 rounded"
          value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })} />
        <input type="email" placeholder="Email" className="border p-2 w-full mb-2 rounded"
          value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
        <input type="password" placeholder="Password" className="border p-2 w-full mb-2 rounded"
          value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} />
        <select className="border p-2 w-full mb-2 rounded"
          value={form.role} onChange={(e) => setForm({ ...form, role: e.target.value })}>
          <option value="student">Student</option>
          <option value="teacher">Teacher</option>
        </select>
        <button className="bg-blue-500 text-white p-2 w-full rounded hover:bg-blue-600">Register</button>
      </form>
    </div>
  );
}