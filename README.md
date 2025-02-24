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

- 📋 **Get All Tasks** — View all tasks, mark as complete, or delete.
- ➕ **Add New Task** — Simple form to add new tasks.

## 🛠️ Tech Stack

- **Backend:** Bottle (Python)
- **Database:** SQLite (via SQLAlchemy)

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
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

### 4️⃣ Open in Browser

```
http://localhost:8080/
```

## 💡 Usage

- **Task List:** View all tasks, mark as complete, or delete them.
- **Add New Task:** Create a new task using the form.

## 📋 API Endpoints

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| GET    | `/tasks`      | Fetch all tasks    |
| POST   | `/tasks`      | Add a new task     |
| PUT    | `/tasks/<id>` | Mark task complete |
| DELETE | `/tasks/<id>` | Delete a task      |

## 💬 Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!

## 📝 License

This project is licensed under the [MIT License](LICENSE).
