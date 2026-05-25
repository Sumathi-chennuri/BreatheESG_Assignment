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

## Backend Setup

Open terminal:

```bash
cd backend
python manage.py runserver
```

Backend URL:

```txt
http://127.0.0.1:8000
```

---

## Frontend Setup

Open terminal:

```bash
cd frontend
npm start
```

Frontend URL:

```txt
http://localhost:3000
```

---

## API Endpoints

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
