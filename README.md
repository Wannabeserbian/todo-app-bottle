# Task Management Admin Panel

This is a **Task Management Admin Panel** built with **Bottle** (Python), **Bootstrap**, and **Axios**. It features an **Admin Dashboard** with the ability to **add, complete, and delete tasks**.

## 📁 Project Structure

```
task_management_app/
│
├── app.py                # Bottle backend (API routes)
├── models.py             # SQLAlchemy models (Task table)
├── task_management.db    # SQLite database
├── requirements.txt      # Python dependencies
│
└── README.md              # Project documentation
```

## ✅ Features

- 📋 **Get All Tasks** — Retrieve all tasks from the system.
- ✏️ **Add New Task** — Create a new task using the API.
- 🔄 **Update Task** — Modify an existing task's details.
- 🗑️ **Delete Task** — Remove a task from the system.

## 🛠️ Tech Stack

- **Backend:** Bottle (Python)
- **Database:** SQLite (via SQLAlchemy)

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Wannabeserbian/todo-app-bottle.git
cd task_management_app
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
python app.py
```

### 4️⃣ Use API in Postman (or anywhere else)

```
http://localhost:8080/
```

## 📋 API Endpoints

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| GET    | `/tasks`      | Fetch all tasks    |
| POST   | `/tasks`      | Add a new task     |
| PUT    | `/tasks/<id>` | Mark task complete |
| DELETE | `/tasks/<id>` | Delete a task      |
