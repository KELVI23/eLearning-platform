"use client";
import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div>

      {/* Hero Section */}
      <header className="bg-primary text-white text-center py-20 px-6">
        <h1 className="text-4xl font-bold mb-4">Learn New Skills Anytime, Anywhere</h1>
        <p className="text-lg mb-6">Join thousands of learners and level up your career with expert-led courses.</p>
        <Link href="/courses" className="btn-secondary">
          Browse Courses
        </Link>
      </header>

      {/* Course Categories */}
      <section className="section">
        <h2 className="section-title">Explore Popular Categories</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {[
          { title: "Web Development", image: "/images/web-development.jpg" },
          { title: "Data Science", image: "/images/data-science.jpg" },
          { title: "Business & Finance", image: "/images/finance.jpg" },
          { title: "Graphic Design", image: "/images/design.jpg" },
          { title: "Cybersecurity", image: "/images/cybersecurity.jpg" },
          { title: "Marketing", image: "/images/marketing.jpg" }
          ].map((category) => (
            <div key={category.title} className="course-card">
              <Image src={category.image} alt={category.title} width={600} height={300} className="w-full h-48 object-cover" />
              <div className="course-card-content">
                <h3 className="course-card-title">{category.title}</h3>
                <Link href="/courses" className="course-card-link">View Courses →</Link>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Benefits Section */}
      <section className="bg-gray-200 dark:bg-gray-800 py-16 px-8 text-center">
        <h2 className="section-title">Why Learn With Us?</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {[
            { icon: "🎓", title: "Expert Instructors", desc: "Learn from industry professionals with real-world experience." },
            { icon: "💡", title: "Flexible Learning", desc: "Access courses anytime, anywhere, at your own pace." },
            { icon: "📜", title: "Certifications", desc: "Earn certificates to boost your resume and career prospects." }
          ].map((benefit) => (
            <div key={benefit.title} className="bg-white dark:bg-gray-700 shadow-lg rounded-lg p-6 text-center">
              <div className="text-4xl">{benefit.icon}</div>
              <h3 className="text-xl font-bold mt-4">{benefit.title}</h3>
              <p className="text-gray-600 dark:text-gray-300 mt-2">{benefit.desc}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}