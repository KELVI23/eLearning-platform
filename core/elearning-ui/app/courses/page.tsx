"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import { Url } from "next/dist/shared/lib/router/router";

interface Course {
  id: number;
  title: string;
  description: string;
  difficulty_level : string;
  image_url : string;
  teacher : string;

}

export default function Courses() {
  
  const [courses, setCourses] = useState<Course[]>([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);


  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/courses/?page=${currentPage}&search=${searchTerm}`)
      .then((res) => res.json())
      .then((data) => {
        setCourses(data.results || []); // Handle paginated API response
        setTotalPages(Math.ceil(data.count / 12)); // Update total pages
      })
      .catch((error) => console.error("Error fetching courses:", error));
  }, [currentPage, searchTerm]);

  return (
    <div className="p-6 min-h-screen bg-gray-800">
      <h1 className="text-3xl font-bold mb-4">Available Courses</h1>

      {/* Search Input */}
      <input
        type="text"
        placeholder="Search courses..."
        className="border p-2 rounded w-half mb-4 text-black"
        value={searchTerm}
        onChange={(e) => {
          setSearchTerm(e.target.value);
          setCurrentPage(1); // Reset to first page on new search
        }}
      />

      {/* Course List */}
      {courses.length === 0 ? (
        <p className="text-gray-500">No courses found.</p>
      ) : (
        <ul className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {courses.map((course) => (
            <li key={course.id} className="border p-3 my-2 rounded shadow bg-white dark:bg-gray-900">
              <img src={course.image_url} alt={course.title} width={400} height={200} className="rounded-md" />
              <h2 className="text-xl font-bold mt-2">{course.title}</h2>
              <p>{course.description}</p>
              <p className="text-gray-300">{course.teacher} | {course.difficulty_level}</p>
              <Link href={`/courses/${course.id}`} className="text-yellow-600">View Course →</Link>
            </li>
          ))}
        </ul>
      )}
      
      {/* Pagination Controls */}
      <div className="flex justify-center mt-6 space-x-4">
        <button
          onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
          disabled={currentPage === 1}
          className="px-4 py-2 dark:bg-gray-300 bg-orange-300 rounded disabled:opacity-50"
        >
          Previous
        </button>
        <span>Page {currentPage} of {totalPages}</span>
        <button
          onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
          disabled={currentPage === totalPages}
          className="px-4 py-2 bg-orange-300 dark:bg-gray-300 rounded disabled:opacity-50">
          Next
        </button>
      </div>
    </div>
  );
}