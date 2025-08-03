from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy login data
students = {
    'S22BDOCS1M01160': {
        'name': 'Neehal',
        'student_id': 'S22BDOCS1M01160',
        'email': 'neehalrafique@gmail.com',
        'class': 'BSCS',
        'courses': [
            {'course_name': 'Math', 'instructor': 'Dr. Tariq', 'grade': 'A'},
            {'course_name': 'Programming', 'instructor': 'Sir Usman', 'grade': 'B+'},
            {'course_name': 'Physics', 'instructor': 'Dr. Farah', 'grade': 'A-'},
        ],
        'notifications': [
            {'message': 'Assignment due tomorrow', 'date': '2025-08-02'},
            {'message': 'Midterm schedule uploaded', 'date': '2025-08-01'},
        ]
    }
}

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in students:
            return redirect(url_for('dashboard', user=username))
        else:
            return "Invalid username!"
    return render_template('login.html')

@app.route('/dashboard/<user>')
def dashboard(user):
    student = students.get(user)
    if not student:
        return "Student not found", 404
    return render_template('dashboard.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
