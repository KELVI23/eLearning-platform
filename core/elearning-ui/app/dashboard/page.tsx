"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";


interface User {
  id: number;
  username: string;
  email: string;
  role: string;
  profile_picture?: string;
  status?: string;
  enrolled_courses?: Course[];
}

interface Course {
  id: number;
  title: string;
  description: string;
  teacher:string;
  image_url: string;
  students: number[]; 
}

interface Status {
  id: number;
  user: string;
  content: string;
  created_at: string;
}

export default function Dashboard() {
  const [user, setUser] = useState<User | null>(null);
  const [courses, setCourses] = useState<Course[]>([]);
  const [studentDetails, setStudentDetails] = useState<Record<number, User>>({});
  const [users, setUsers] = useState<User[]>([]);
  const [statuses, setStatuses] = useState<Status[]>([]);
  const [searchQuery, setSearchQuery] = useState("");
  const router = useRouter();

  useEffect(() => {
    const fetchUser = async () => {
      const token = localStorage.getItem("access_token");
      if (!token) {
        router.push("/login");
        return;
      }

      // Fetch user profile including enrolled courses
      try {
        const res = await fetch("http://127.0.0.1:8000/api/profile/?include_courses=true", {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (!res.ok) {
          throw new Error("Failed to fetch user profile");
        }

        const data = await res.json();
        setUser(data);

        // Fetch enrolled or taught courses based on role
        if (data.role === "teacher") {
          searchUsers(token);
          fetchTaughtCourses(token);
        } else {
          fetchEnrolledCourses(token);
        }
      } catch (error) {
        console.error("Error fetching user profile:", error);
      }
    };

    fetchUser();
  }, []);

  // Fetch all users
  const searchUsers = async (token: string) => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/users/", {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!res.ok) throw new Error("Failed to fetch users");

      const data = await res.json();
      setUsers(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error("Error fetching users:", error);
      setUsers([]);
    }
  };

  useEffect(() => {
    const fetchStatuses = async () => {
      const token = localStorage.getItem("access_token");
      if (!token) {
        console.warn("No token found, user is not authenticated.");
        return;
      }
  
      try {
        const res = await fetch("http://127.0.0.1:8000/api/statuses/", {
          headers: { Authorization: `Bearer ${token}` },
        });
  
        if (!res.ok) {
          throw new Error("Failed to fetch statuses");
        }
  
        const data = await res.json();
        setStatuses(Array.isArray(data) ? data : []);
      } catch (error) {
        console.error("Error fetching statuses:", error);
        setStatuses([]); // Prevent crashing map()
      }
    };
  
    fetchStatuses();
  }, []);

    // Fetch enrolled courses (for students)
    const fetchEnrolledCourses = async (token: string) => {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/courses/?enrolled=true", {
          headers: { Authorization: `Bearer ${token}` },
        });
    
        const data = await res.json();
        console.log("Enrolled Courses Response:", data.results); // Debugging
    
        setCourses(Array.isArray(data.results) ? data.results : []); // Extract results
      } catch (error) {
        console.error("Error fetching enrolled courses:", error);
        setCourses([]);
      }
    };

    // Fetch courses taught by teacher
    const fetchTaughtCourses = async (token: string) => {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/courses/?taught_by_me=true", {
          headers: { Authorization: `Bearer ${token}` },
        });
    
        const data = await res.json();
        console.log("Taught Courses Response:", data.results); // Debugging
    
        setCourses(Array.isArray(data.results) ? data.results : []); // Extract results
      } catch (error) {
        console.error("Error fetching taught courses:", error);
        setCourses([]);
      }
    };

    // Fetch full student details from API
    const fetchStudentDetails = async (studentIds: number[]) => {
      const token = localStorage.getItem("access_token");

      const students = await Promise.all(
        studentIds.map(async (id) => {
          const res = await fetch(`http://127.0.0.1:8000/api/users/${id}/`, {
            headers: { Authorization: `Bearer ${token}` },
          });
          return res.ok ? await res.json() : null;
        })
      );

      // Store details in state
      setStudentDetails((prev) => ({
        ...prev,
        ...Object.fromEntries(students.filter(Boolean).map((s) => [s.id, s])),
      }));
    };

    // Fetch student details when courses load
    useEffect(() => {
      if (courses.length > 0) {
        const studentIds = courses.flatMap((course) => course.students);
        fetchStudentDetails(studentIds);
      }
    }, [courses]);

  if (!user) return <div className="text-center p-6">Loading...</div>;

  return (
    <div className="p-6 min-h-screen bg-gray-100 dark:bg-gray-800">
      <div className="flex items-center gap-4 mb-6">
      {user.profile_picture && ( <img src={user.profile_picture} alt="Profile"className="w-28 h-26 rounded-full"
        onError={(e) => console.error("Image Load Error:", e.currentTarget.src)}  // Debugging
      />  
      )}
        <div>
          <h1 className="text-3xl font-bold">Welcome, {user.username}</h1> 
          <p className="text-gray-500">{user.email}</p>
        </div>
      </div>

      {/* Status Section - Displays the latest status or "No status set" */}
      <h3 className="text-x font-bold mb-4">Recent Status Updates</h3>
      <div className="flex items-center gap-4 mb-10 bg-white dark:bg-gray-700 p-3 rounded-lg shadow">
        <p className="text-black-600 dark:text-gray-100 text-m mr-40">
          {statuses.length > 0 ? `${statuses[0].content} ••• ${new Date(statuses[0].created_at).toLocaleString()}`
            : "No status set"}
        </p>
        <button
          onClick={() => router.push("/statuses")}
          className="px-3 py-1 bg-yellow-500 text-white text-sm rounded hover:bg-yellow-600"
        >
          Edit
        </button>
      </div>
     
      {/* My Account Button */}
      <Link href="/account" className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 mr-60 mb-40">
        My Account
      </Link>

      {/* Go to chat button */} 
      <Link href="/chat" className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"> 
       Go to chat
      </Link>

      {/* Student Dashboard */}
      {user.role === "student" && (
        <div className="mt-6">
          <h2 className="text-2xl font-bold mb-4">My Enrolled Courses</h2>
          {courses.length === 0 ? (
            <p className="text-gray-500">You are not enrolled in any courses yet.</p>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {courses.map((course) => (
                <div key={course.id} className="bg-white shadow-md rounded-lg overflow-hidden">
                  <img src={course.image_url} alt={course.title} className="w-full h-48 object-cover" />
                  <div className="p-4">
                    <h3 className="text-xl font-bold">{course.title}</h3>
                    <p className="text-gray-500">{course.description}</p>

                    {/* Buttons Container */}
                    <div className="mt-2 flex space-x-6">
                      {/* View Course Button */}
                      <Link href={`/courses/${course.id}/materials`} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
                        View Course
                      </Link>

                      {/* Give Feedback Button */}
                      <Link href={`/feedback/${course.id}`} className="px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600">
                        Give Feedback
                      </Link>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Teacher Dashboard */}
      {user.role === "teacher" && (
        <div className="mt-6">
          {/* Search Bar for Users */}
          <input type="text" placeholder="Search for students or teachers..." className="text-black border p-2 rounded w-80 mb-4"
            value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)}
          />

          {/* Filtered User List */}
          {searchQuery && (
            <div className="dark:bg-white bg-gray-600 p-4 rounded-lg shadow mb-6 text-black w-80">
              <h3 className="text-xl font-bold mb-2">Search Results</h3>
              {users
                .filter((u) => u.username.toLowerCase().includes(searchQuery.toLowerCase()))
                .slice(0, 3) // Limit to 3 users
                .map((filteredUser) => (
                  <div key={filteredUser.id} className="flex justify-between items-center p-2 border-b">
                    <span className="text-gray-700">{filteredUser.username} ({filteredUser.role})</span>
                  </div>
                ))}
              {users.filter((u) => u.username.toLowerCase().includes(searchQuery.toLowerCase())).length === 0 && (
                <p className="text-gray-500">No users found.</p>
              )}
            </div>
          )}

          {/* Courses Section */}
          <h2 className="text-2xl font-bold mb-4">Courses I Teach</h2>
          {courses.length === 0 ? (
            <p className="text-gray-500">You are not teaching any courses yet.</p>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {courses.map((course) => (
                <div key={course.id} className="bg-white shadow-md rounded-lg overflow-hidden">
                  <img src={course.image_url} alt={course.title} className="w-full h-48 object-cover" />
                  <div className="p-4">
                    <h3 className="text-xl font-bold">{course.title}</h3>
                    <p className="text-gray-500">{course.description}</p>
                    <Link href={`/courses/${course.id}/materials`} className="text-blue-600 hover:underline mt-2 block">
                      Manage Course →
                    </Link>

                    {/* Student Management */}
                    <div className="mt-8">
                      <h4 className="text-lg font-bold bg-blue-500">Enrolled Students</h4>
                      {course.students.length > 0 ? (
                        <ul className="mt-2">
                          {course.students.map((studentId) => {
                            const student = studentDetails[studentId];

                            return student ? (
                              <li key={student.id} className="flex justify-between items-center border-b py-2 text-black bg-gray-200 px-4">
                                <span>{student.username}</span>
                                <button className="px-2 py-1 text-sm bg-red-500 text-white rounded"
                                  onClick={() => handleRemoveStudent(course.id, student.id)}>
                                  Remove
                                </button>
                              </li>
                            ) : null; // If student details are missing, don't render anything
                          })}
                        </ul>
                      ) : (
                        <p className="text-gray-600 mt-2">No students enrolled yet.</p>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
          {/* Add Course Button */}
          <Link href="/courses/create" className="px-4 py-2 mt-4 bg-green-600 text-white rounded hover:bg-green-700">
            Add New Course
          </Link>
        </div>
      )}
    </div>
  );
}

// Remove students from a course
const handleRemoveStudent = async (courseId: number, studentId: number) => {
  const token = localStorage.getItem("access_token");
  if (!token) return;

  const res = await fetch(`http://127.0.0.1:8000/api/courses/${courseId}/remove_student/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ student_id: studentId }),
  });

  if (res.ok) {
    alert("Student removed successfully.");
    window.location.reload();
  } else {
    alert("Failed to remove student.");
  }
};

