# eLearnHub - An Advanced eLearning Platform

## 📌 Overview
**eLearnHub** is a **full-stack eLearning platform** that enables teachers to create courses and students to enroll, interact, and submit assignments. Features:

✅ **Django & PostgreSQL Backend** for robust data management  
✅ **Next.js Frontend** with TailwindCSS for a modern UI  
✅ **JWT Authentication** with role-based access for teachers & students  
✅ **WebSockets (Django Channels + Redis)** for real-time chat & notifications  
✅ **Google Drive API Integration** for secure course material storage  
✅ **OpenAPI (Swagger) Documentation** for easy API access  
✅ **Celery Task Queue** for background processing  

## 🏗️ Tech Stack
**Frontend:** Next.js (React), TailwindCSS  
**Backend:** Django, Django REST Framework, PostgreSQL  
**Real-time:** Django Channels, Redis, WebSockets  
**Authentication:** JWT, Django Authentication  
**File Storage:** Google Drive API  
**Asynchronous Processing:** Celery, Redis  

---
## 🚀 Features
### 🔹 User Roles
👨‍🏫 **Teachers**: Create, manage courses, and upload course materials.  
🎓 **Students**: Enroll in courses, submit assignments, and participate in discussions.  

### 🔹 Course Management
📚 **Course Creation & Enrollment**: Teachers create courses; students can enroll.  
📂 **Course Materials**: Upload videos, PDFs, and more via **Google Drive API**.  
📑 **Assignments & Submissions**: Teachers assign tasks; students submit work.  

### 🔹 Interactive Learning
💬 **Real-time Chat & Notifications**: Powered by **Django Channels + Redis**.  
🔔 **Live Updates**: Notifications for enrollments, messages, and announcements.  

### 🔹 API & Documentation
📜 **RESTful API**: Built with Django REST Framework.  
📖 **OpenAPI & Swagger Docs**: Auto-generated API documentation.  

---
## ⚙️ Installation & Setup
### 📌 Prerequisites
- **Python 3.3+** & **Node.js 18+**
- **PostgreSQL & Redis**
- **Google Cloud Service Account** (for Google Drive API)

### 🔹 Backend Setup
```bash
# Clone the repository
git clone https://github.com/KELVI23/elearnhub.git && cd elearnhub

# Create virtual environment & activate it
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables (Update .env file)
cp .env.example .env  # Update with your values

# Apply database migrations
python manage.py migrate

# Create a superuser (admin)
python manage.py createsuperuser

# Run Celery Worker
celery -A config worker --loglevel=info

# Start Redis (if not already running)
redis-server

# Start Django server
python manage.py runserver
```

### 🔹 Frontend Setup
```bash
cd core/elearning-ui  # Navigate to frontend

# Install dependencies
npm install

# Start Next.js frontend
npm run dev
```

---
## 🔍 API Documentation
📌 **Generate OpenAPI Schema & Swagger UI**
```bash
python manage.py spectacular --color --file openapi-schema.yml
```
Access API Docs at:
- **Swagger UI**: [`http://127.0.0.1:8000/api/docs/`](http://127.0.0.1:8000/api/docs/)
- **Redoc**: [`http://127.0.0.1:8000/api/redoc/`](http://127.0.0.1:8000/api/redoc/)

---
## 🚀 Deployment (Future Plans)
- **Containerized Deployment**: Docker + Docker Compose  
- **CI/CD Pipeline**: GitHub Actions for automated testing & deployment  
- **Cloud Hosting**: AWS/GCP for scalability  

---
## 📜 License
This project is licensed under the **MIT License**.

---
## 📞 Contact & Contributions
👤 **Kelvin Musodza**  
🔗 GitHub: [@KELVI23](https://github.com/KELVI23)  

Contributions are welcome! Feel free to submit issues or pull requests. 🚀

