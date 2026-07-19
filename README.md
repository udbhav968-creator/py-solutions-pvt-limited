# 🏥 Pure Health Clinic - Enterprise Backend API

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-092E20.svg)
![DRF](https://img.shields.io/badge/DRF-3.15+-red.svg)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-black.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2ea44f.svg)

Welcome to the enterprise-grade backend repository for the **Healthcare Clinic Website**. This system was architected and developed during the PY Digital Services Pvt. Ltd. internship.

> **Live API Documentation**: [https://pysolutionss.vercel.app/api/docs/](https://pysolutionss.vercel.app/api/docs/)

---

## 👨‍💻 Backend Team & Module Ownership

| Module Owner | Assignment | Responsibilities |
| :--- | :--- | :--- |
| **Thota Harshavardhan Reddy** | *Authentication* | JWT Auth, RBAC, Admin/User Login |
| **Alok Verma** | *Appointments* | Booking APIs, Doctor Availability |
| **Aniket Ghatage** | *Content* | Blogs, Services, Galleries, Testimonials |
| **Udbhav** | *Integration & Core* | Base Architecture, CI/CD, Admin Dashboards, API Docs, Exception Handling |

---

## 🏗️ Enterprise Architecture & Custom Innovations

This backend was built to exceed basic requirements and simulate a true **Level 3 RESTful standard** industry environment. The Integration Module (Udbhav) introduced the following advanced customizations:

### 1. Abstract Base Models & Soft Deletions (`TimeStampedModel`)
Instead of permanently deleting medical records (which violates healthcare compliance), all models inherit from an abstract base class.
- **UUIDv4 Primary Keys**: Replaced auto-incrementing integers (`id=1`) with secure UUIDs to prevent ID Enumeration attacks (e.g., guessing another patient's ID).
- **Soft Deletes**: Implementing an `is_deleted` boolean. When a record is "deleted", it is simply hidden from normal queries, preserving historical audit logs.

### 2. CI/CD Pipeline (GitHub Actions)
Continuous Integration (CI) has been fully configured. Every push to the `main` branch automatically triggers a GitHub Actions runner that provisions a Linux server, installs dependencies, and runs the automated test suite across multiple Python versions to guarantee stability.

### 3. Advanced Error Handling Middleware
Standard Django errors are inconsistent. We engineered a `custom_exception_handler` that overrides DRF's default behavior. Whether it's a 404, a validation error, or a 500 Server Crash, the API *always* returns a highly predictable, flattened JSON response:
```json
{
  "success": false,
  "errors": ["This field is required.", "Invalid date format."]
}
```

### 4. Zero-Trust Secrets Management
Hardcoded secrets are a massive security risk. We integrated `django-environ` and separated all configuration logic into `.env` files. The production `SECRET_KEY` and `DATABASE_URL` are injected purely at runtime via Vercel environment variables.

### 5. High-Performance Dashboard Analytics
The `/api/admin/dashboard/` endpoint was optimized using advanced Django ORM aggregations (`Count`, `Q` filters) to calculate complex metrics (total users, active appointments, recent inquiries) in a *single database hit* rather than looping through records in Python memory.

---

## 🚀 Deployment (Vercel Serverless)

This API is actively deployed on Vercel's serverless edge network.

**Important Note regarding the Root URL (`/`)**: 
Because this is a decoupled headless API, visiting the root domain will return a `404 Page Not Found` error. This is intentional. To interact with the system, visit the API routes:

- **Swagger UI**: [`/api/docs/`](https://pysolutionss.vercel.app/api/docs/)
- **ReDoc**: [`/api/redoc/`](https://pysolutionss.vercel.app/api/redoc/)

### Deploying Your Own Instance:
1. Clone the repository and import it into Vercel.
2. In the Vercel Dashboard, set the `DEBUG` environment variable to `False`.
3. Provide a remote PostgreSQL/MySQL string via the `DATABASE_URL` environment variable. *(Note: Vercel's filesystem is read-only, so SQLite will fail upon write operations in production).*

---

## 💻 Local Development Setup

We have included a `Makefile` for developer convenience.

### Installation
```bash
# Clone the repository
git clone https://github.com/udbhav968-creator/py-solutions-pvt-limited.git
cd clinic_backend

# Create a virtual environment and activate it
python -m venv venv
source venv/Scripts/activate  # On Windows

# Install dependencies using Make
make install
```

### Environment Config
Create a `.env` file in the root directory:
```ini
DEBUG=True
SECRET_KEY=local-development-secret-key-123
```

### Run Server & Tests
```bash
# Run migrations
make migrate

# Start the server
make run

# Run automated tests
make test
```
