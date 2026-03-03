# Student Record Manager 🚀
### Python | OOP | Hashmap | CSV | CLI

A CLI-based Student Record Manager built with Python using Object-Oriented Programming (OOP) and Hashmaps (Dictionary) for efficient O(1) student lookup, with CSV file persistence.

---

## 🚀 Features

- Add Student
- Search Student by ID (O(1) lookup)
- Update Student Marks
- Display All Students
- Save Records to CSV
- Load Records from CSV
- Input Validation & Error Handling

---

## 🧠 Concepts Used

- Classes & Objects
- Constructors (`__init__`)
- Encapsulation
- Dictionary (Hashmap)
- File Handling (CSV)
- Exception Handling
- CLI-based Menu System

---

## 🏗️ Project Structure
├── srm.py # Core logic (Student & StudentManager classes)
├── main.py # CLI interface
├── students.csv # Data storage (auto-created)
└── README.md

---

## ⚡ Time Complexity Analysis

| Operation              | Time Complexity |
|------------------------|-----------------|
| Add Student            | O(1)            |
| Search Student (by ID) | O(1)            |
| Update Marks           | O(1)            |
| Display All Students   | O(n)            |
| Save to CSV            | O(n)            |
| Load from CSV          | O(n)            |

Dictionary ensures constant-time lookup for student search and update operations.

---

## ▶️ How to Run

1. Clone the repository:
https://github.com/ms-cry/student-record-manager.git
2. Navigate to the project folder:

cd student-record-manager

3. Run the program:

python main.py


---

## 📌 Example Menu


--- Student Record Manager ---

Add Student

Search Student

Update Marks

Save & Exit

Display All Students


---

## 📚 What This Project Demonstrates

This project demonstrates practical application of:
- OOP design principles
- Efficient data handling using Hashmaps
- Persistent storage using CSV files
- Clean CLI interaction flow
- Input validation and structured error handling

---

## 🔥 Future Improvements

- Delete Student feature
- Sorting by marks
- Grade calculation system
- GUI version (Tkinter / Web App)
- Database integration (SQLite/PostgreSQL)

---

## 👨‍💻 Author

Built as part of structured AI & Data Structures learning roadmap.
