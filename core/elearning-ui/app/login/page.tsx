"use client";
import { useState, useContext } from "react";
import { useRouter } from "next/navigation";
import { AuthContext } from "../context/AuthContext";

export default function Login() {
  const [form, setForm] = useState({ username: "", password: "" });
  const router = useRouter();
  const { login } = useContext(AuthContext); // Use login function from context

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch("http://127.0.0.1:8000/api/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    if (res.ok) {
      const data = await res.json();
      login({ username: form.username }, data.access, data.refresh); // Immediately update UI
      router.push("/dashboard");
    } else {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center dark:bg-gray-500 bg-gray-100">
      <form onSubmit={handleLogin} className="bg-white dark:bg-gray-800 p-6 rounded shadow-md w-96">
        <h2 className="text-2xl font-bold mb-4 text-center">Login</h2>
        <input type="text" placeholder="Username" className="text-black border p-2 w-full mb-2 rounded" 
        value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })}/>
        <input type="password" placeholder="Password" className="text-black border p-2 w-full mb-2 rounded"
          value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })}/>
        <button className="bg-blue-500 text-white p-2 w-full rounded hover:bg-blue-600">
          Login
        </button>
      </form>
    </div>
  );
}