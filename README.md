# attendance-scheduler
# 📅 Attendance Scheduler API

A scalable backend system for managing **group-based time slot bookings**, built with **Flask**, **SQLAlchemy**, and **PostgreSQL**, using **Dependency Injection (DI)** and the **Repository Pattern**.

---

## 🚀 Features

* Create and manage **groups** with capacity limits
* Create **time slots** for scheduling
* Book slots with **concurrency safety**
* Prevent **overbooking** using row-level locking
* Clean architecture using:

  * Service Layer (business logic)
  * Repository Layer (data access)
  * DI container (dependency management)

---

## 🏗️ Architecture

```
app/
├── models/          # SQLAlchemy models
├── repositories/    # DB access layer
├── services/        # Business logic
├── routes/          # Flask controllers (API)
├── container.py     # Dependency Injection setup
├── extensions.py    # DB + Migrate instances
```

### Flow

```
Route → Service → Repository → Database
```

---

## 🧱 Tech Stack

* Python 3.9+
* Flask
* SQLAlchemy
* PostgreSQL
* Flask-Migrate (Alembic)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo

```bash
git clone <your-repo-url>
cd attendance-scheduler
```

---

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure environment

Set your database URI:

```bash
export DATABASE_URL=postgresql://attendance_user:devpass@localhost/attendance_db
export FLASK_APP=main.py
```

---

### 5️⃣ Run migrations

Using Flask-Migrate:

```bash
flask db init      # first time only
flask db migrate -m "init"
flask db upgrade
```

---

### 6️⃣ Run the app

```bash
flask run
```

App runs at:

```text
http://localhost:5000
```

---

## 📌 API Endpoints

### ➕ Create Group

```http
POST /groups
```

```json
{
  "name": "Fitness Group",
  "capacity": 10
}
```

---

### ➕ Create Time Slot

```http
POST /timeslots
```

```json
{
  "start_time": "2026-04-01T10:00:00",
  "end_time": "2026-04-01T11:00:00",
  "group_id": 1
}
```

---

### 📥 Get Time Slots

```http
GET /timeslots
```

---

### 📅 Book a Slot

```http
POST /bookings
```

```json
{
  "user_id": 1,
  "timeslot_id": 1
}
```

---

## 🔐 Concurrency Handling

To prevent overbooking:

```python
.with_for_update()
```

* Locks the row at DB level
* Ensures atomic booking operations
* Prevents race conditions

---

## 🧪 Sample cURL

```bash
curl -X POST http://localhost:5000/timeslots \
  -H "Content-Type: application/json" \
  -d '{
    "start_time": "2026-04-01T10:00:00",
    "end_time": "2026-04-01T11:00:00",
    "group_id": 1
  }'
```

---

## 🐛 Common Issues

### ❌ `ModuleNotFoundError: flask_migrate`

```bash
pip install Flask-Migrate
```

---

### ❌ `role does not exist`

Create DB user:

```sql
CREATE ROLE attendance_user WITH LOGIN PASSWORD 'devpass';
ALTER ROLE attendance_user CREATEDB;
```

---

### ❌ Foreign key errors

Ensure parent records exist:

* Create `Group` before `TimeSlot`

---

## 🧠 Design Patterns Used

* **Repository Pattern** → isolates DB logic
* **Service Layer** → handles business rules
* **Dependency Injection** → clean, testable code
* **Unit of Work (SQLAlchemy session)**

---

## 🚀 Future Improvements

* Authentication & authorization (JWT)
* Recurring time slots
* Timezone handling (UTC storage)
* Rate limiting for bookings
* Admin dashboard

---

## 👨‍💻 Author

Built by Olusegun Jayesimi

---

## 📄 License

MIT License

