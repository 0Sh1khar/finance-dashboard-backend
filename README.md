# Finance Data Processing and Access Control Backend

A backend system built for a finance dashboard with secure authentication, role-based access control, financial record management, and dashboard analytics.

---

## Live API

Base URL: `https://findb.onrender.com`  
Swagger Docs: [https://findb.onrender.com/docs](https://findb.onrender.com/docs)

---

## Tech Stack

- FastAPI
- SQLite
- SQLAlchemy
- JWT Authentication
- Pydantic
- bcrypt

---

## Assumptions

- SQLite is used for simplicity as permitted by the assignment
- JWT token is required for all endpoints except `/auth/register` and `/auth/login`
- Role is assigned at registration time
- An inactive user cannot log in or access any protected endpoint

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
- Fields: amount, type (income/expense), category, date, notes

### Dashboard APIs
- Total income
- Total expense
- Net balance
- Category summary
- Monthly trend

---

## Roles & Permissions

| Action | Viewer | Analyst | Admin |
|--------|--------|---------|-------|
| GET /records/ | ✅ | ✅ | ✅ |
| POST /records/ | ❌ | ✅ | ✅ |
| PUT /records/{id} | ❌ | ❌ | ✅ |
| DELETE /records/{id} | ❌ | ❌ | ✅ |
| GET /dashboard/summary | ✅ | ✅ | ✅ |
| GET /dashboard/category-summary | ✅ | ✅ | ✅ |
| GET /dashboard/monthly-trend | ✅ | ✅ | ✅ |

---

## How to Test (Swagger UI)

1. Open [https://findb.onrender.com/docs](https://findb.onrender.com/docs)

2. Register a user via `POST /auth/register`.
   Use any of the following test accounts:

   **Analyst account:**
```json
   {
     "name": "Shikhar",
     "email": "shikhar@gmail.com",
     "password": "123456",
     "role": "analyst"
   }
```

   **Admin account:**
```json
   {
     "name": "Admin",
     "email": "admin@test.com",
     "password": "123456",
     "role": "admin"
   }
```

   **Viewer account:**
```json
   {
     "name": "Viewer",
     "email": "viewer@test.com",
     "password": "123456",
     "role": "viewer"
   }
```

3. Login via `POST /auth/login`:
```json
   {
     "email": "shikhar@gmail.com",
     "password": "123456"
   }
```

4. Copy the `access_token` from the login response

5. Click the **Authorize 🔒** button at the top of the Swagger page

6. Paste the token as: `Bearer <your_token>`

7. Now all protected endpoints are unlocked — test away!

> 💡 Tip: To test role-based restrictions, log in with different accounts and try actions that should be blocked. For example, a Viewer trying `POST /records/` should get a 403 Forbidden response.

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

Swagger docs available at:
```text
http://127.0.0.1:8000/docs
```
