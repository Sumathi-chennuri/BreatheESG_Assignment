# Breathe ESG Assignment

## Project Overview

This project is an ESG Data Management Dashboard built using Django and React.

The application allows users to:

- View ESG activity records
- Manage records through Django Admin
- Upload ESG data using CSV files
- Display uploaded data in a React dashboard

---

## Tech Stack

### Backend
- Django
- Django REST Framework
- SQLite

### Frontend
- React
- Axios

---

## Features

- Django REST API
- React Dashboard UI
- CSV Upload
- Admin Panel
- Data Listing Table
- API Integration

---

# How to Run the Project

## 1. Clone Repository

Open terminal:

```bash
git clone https://github.com/Sumathi-chennuri/BreatheESG_Assignment.git
```

Move into project:

```bash
cd BreatheESG_Assignment
```

---

## 2. Backend Setup

Go to backend:

```bash
cd backend
```

Install packages:

```bash
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install pandas
```

Run migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

Run backend server:

```bash
python manage.py runserver
```

Backend URL:

```txt
http://127.0.0.1:8000
```

Admin URL:

```txt
http://127.0.0.1:8000/admin
```

---

## 3. Frontend Setup

Open another terminal.

Go to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
npm install axios
```

Run React server:

```bash
npm start
```

Frontend URL:

```txt
http://localhost:3000
```

---

## 4. API Endpoints

Get Records:

```txt
GET /api/records/
```

Upload CSV:

```txt
POST /api/upload/
```

---

## Project Structure

```txt
BreatheESG_Assignment
│
├── backend
├── frontend
├── README.md
├── DECISION.md
├── MODEL.md
├── SOURCES.md
└── TRADEOFFS.md
```
