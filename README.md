==================================================
STUDENT DASHBOARD - FLASK BASED WEB APPLICATION
==================================================

📌 DESCRIPTION:
This is a simple Student Dashboard web application built using Flask. 
It shows basic student details, enrolled courses, grades, and notifications. 
The data is hardcoded (no database used).

--------------------------------------------------

📁 FOLDER STRUCTURE:

student_dashboard/
│
├── app.py                 → Main Flask application
├── static/
│   └── style.css          → Optional custom styling
│
├── templates/
│   ├── layout.html        → Base HTML layout
│   ├── login.html         → Login page template
│   └── dashboard.html     → Main dashboard view

--------------------------------------------------

⚙️ REQUIREMENTS:

- Python 3.x
- Flask

Install Flask using pip if not already installed:
> pip install flask

--------------------------------------------------

🚀 HOW TO RUN:

1. Open terminal or command prompt.
2. Navigate to the folder:
> cd student_dashboard

3. Run the Flask app:
> python app.py

4. Open your browser and visit:
> http://127.0.0.1:5000/

--------------------------------------------------

👤 LOGIN INFO:

Use the following username to log in:

Username: In this code i write my roll number (S22BDOCS1M01160)  You can change what you want to declare variable

(Password not required — simplified for demo)

--------------------------------------------------

📚 FEATURES:

- Simple login (no password)
- Dashboard with:
  - Student profile information
  - Table of enrolled courses and grades
  - List of notifications
- Bootstrap styling
- Optional custom CSS in `static/style.css`

--------------------------------------------------

🛠️ NEXT FEATURES TO ADD:

- Real login system (Flask-Login)
- Database connection (Flask-SQLAlchemy)
- Chart.js for visual graphs
- Edit or update student data

--------------------------------------------------

🧑‍💻 DEVELOPER NOTES:

This app is for learning purposes and can be extended for real-world student management systems.

Happy Coding! 🎓
