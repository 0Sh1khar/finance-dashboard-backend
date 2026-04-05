# Finance Data Processing and Access Control Backend

A backend system built for a finance dashboard with secure authentication, role-based access control, financial record management, and dashboard analytics.

---

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- JWT Authentication
- Pydantic
- bcrypt

---

## Features

### User Management
- User registration
- Login with JWT
- Role-based access
- Active/inactive users

### Roles
- **Viewer** → read-only access
- **Analyst** → records + insights
- **Admin** → full CRUD access

### Financial Records
- Create records
- View records
- Update records
- Delete records
- Filter by type/category

### Dashboard APIs
- Total income
- Total expense
- Net balance
- Category summary
- Monthly trend

---

## API Endpoints

### Authentication
```http
POST /auth/register
POST /auth/login
```

### Records
```http
POST /records/
GET /records/
PUT /records/{id}
DELETE /records/{id}
```

### Dashboard
```http
GET /dashboard/summary
GET /dashboard/category-summary
GET /dashboard/monthly-trend
```

---

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## Documentation
Swagger docs available at:

```text
http://127.0.0.1:8000/docs
```