# 🏥 Healthcare Clinic Backend API

Welcome to the backend repository for the **Healthcare Clinic Website**! This project was developed as part of the internship assignment at **PY Digital Services Pvt. Ltd.** by the backend team.

Our primary focus while building this infrastructure was to create a highly robust, scalable, and **industry-standard** RESTful API that handles real-world clinic operations effortlessly.

---

## 👨‍💻 Meet the Team & Module Owners

This project is a collaborative effort, divided into four core modules to ensure clean architecture and separation of concerns:

- **Thota Harshavardhan Reddy** 🔐 - *Authentication & User Management*
- **Alok Verma** 📅 - *Appointment Management*
- **Aniket Ghatage** 📄 - *Content Management APIs*
- **Udbhav** ⚙️ - *Administration & System Integration*

---

## 🏗️ Architecture & Industry-Level Upgrades

We didn't just build a standard Django app; we engineered this backend with **production-readiness** in mind. Here are the key industry-level architectural decisions implemented by the Integration team (Udbhav):

1. **Security First (UUIDs & Environ)**:
   - Migrated all database primary keys from predictable integers to **UUIDv4** to prevent ID enumeration attacks.
   - Strict secrets management using `django-environ` and `.env` files to keep credentials out of version control.
2. **Data Integrity (Soft Deletions)**:
   - Introduced a global abstract `TimeStampedModel`.
   - Records are never permanently deleted (`is_deleted` flag), preventing accidental data loss and maintaining historical integrity for audits.
3. **Advanced API Resilience**:
   - Built a highly structured, custom DRF exception handler that flattens validation errors into a predictable JSON schema (`{"success": false, "errors": [...]}`).
   - Configured global rate limiting (Throttling) and Pagination to prevent DDoS and memory overloads.
4. **Performance Optimization**:
   - Implemented Django view caching for the Admin Dashboard to reduce DB load.
   - Utilized complex ORM Aggregations (`Count`, `filter`) for deep analytics on the admin panel.

---

## 🛠️ Technology Stack

- **Language**: Python 3.10+
- **Framework**: Django 5.x
- **API Framework**: Django REST Framework (DRF)
- **Database**: SQLite (Configured for easy migration to MySQL/PostgreSQL via env)
- **Authentication**: Simple JWT (JSON Web Tokens)
- **Documentation**: Swagger UI & ReDoc (via `drf-spectacular`)

---

## 🚀 Getting Started (Local Development)

Follow these steps to get the server running on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/udbhav968-creator/py-solutions-pvt-limited.git
cd clinic_backend
```

### 2. Environment Setup
Create a virtual environment and install dependencies:
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and configure it:
```ini
DEBUG=True
SECRET_KEY=your-super-secret-local-key
```

### 4. Database Migrations
Run the migrations to build the database schema:
```bash
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
```
The API is now running at `http://127.0.0.1:8000/`.

---

## 🚀 Deployment (Vercel)

This project is fully configured for serverless deployment on **Vercel**. 

1. Import your GitHub repository into the Vercel Dashboard.
2. Under **Environment Variables**, add:
   - `DEBUG`: `False`
   - `SECRET_KEY`: `<generate-a-secure-key>`
   - `DATABASE_URL`: `<your-remote-postgres-mysql-url>`
3. Click **Deploy**.

> **⚠️ CRITICAL: Database limitation on Vercel**
> Vercel has an ephemeral filesystem. You **must** provide a remote `DATABASE_URL` (like Supabase, Neon, AWS RDS, or PlanetScale) in your Vercel project environment variables. If you do not provide one, the application will fall back to SQLite, which will fail to persist data upon any write operations!

---

## 📚 API Documentation

We use automated OpenAPI schema generation. Once the server is running, you can explore and test the endpoints directly from your browser:

- **Swagger UI**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **ReDoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- **Postman**: Import the `Postman_Collection.json` located in the root directory.

---

## 🧪 Testing

We value reliability. To run the automated unit test suite:
```bash
python manage.py test
```
