from flask import Flask, render_template, request, redirect, url_for, flash
from student import StudentManager
from exam import ExamManager
from transport import TransportManager
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

# Initialize Managers
student_mgr = StudentManager()
exam_mgr = ExamManager()
transport_mgr = TransportManager()

# Load data on startup
student_mgr.load_from_file()
exam_mgr.load_from_file()
transport_mgr.load_from_file()
transport_mgr.load_queue_from_file()

@app.route('/')
def index():
    return render_template('index.html', 
                           student_count=student_mgr.count, 
                           exam_count=exam_mgr.count, 
                           transport_count=transport_mgr.count)

# --- Student Routes ---
@app.route('/students')
def students():
    students_list = []
    current = student_mgr.head
    while current:
        students_list.append(current)
        current = current.next
    return render_template('students.html', students=students_list)

@app.route('/students/add', methods=['POST'])
def add_student():
    try:
        student_id = int(request.form['student_id'])
        name = request.form['name']
        department = request.form['department']
        phone = request.form['phone']
        email = request.form['email']
        
        success, message = student_mgr.create_student(student_id, name, department, phone, email)
        if success:
            student_mgr.save_to_file()
            flash(message, 'success')
        else:
            flash(message, 'error')
    except ValueError:
        flash("Invalid input format!", 'error')
        
    return redirect(url_for('students'))

@app.route('/students/delete/<int:student_id>')
def delete_student(student_id):
    student_mgr.delete_node(student_id)
    student_mgr.save_to_file()
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('students'))

# --- Exam Routes ---
@app.route('/exams')
def exams():
    return render_template('exams.html', exams=exam_mgr.records)

@app.route('/exams/add', methods=['POST'])
def add_exam():
    try:
        student_id = int(request.form['student_id'])
        student_name = request.form['student_name']
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        marks = float(request.form['marks'])
        
        success, message = exam_mgr.create_exam_record(student_id, student_name, course_code, course_name, marks)
        if success:
            exam_mgr.save_to_file()
            flash(message, 'success')
        else:
            flash(message, 'error')
    except ValueError:
        flash("Invalid input format!", 'error')
        
    return redirect(url_for('exams'))

# --- Transport Routes ---
@app.route('/transport')
def transport():
    transport_list = []
    current = transport_mgr.head
    while current:
        transport_list.append(current)
        current = current.next
        
    queue_list = list(transport_mgr.request_queue)
    
    return render_template('transport.html', transport_list=transport_list, queue_list=queue_list)

@app.route('/transport/register', methods=['POST'])
def register_transport():
    try:
        student_id = int(request.form['student_id'])
        student_name = request.form['student_name']
        route_number = int(request.form['route_number'])
        route_name = request.form['route_name']
        driver_name = request.form['driver_name']
        driver_phone = request.form['driver_phone']
        pickup_time = request.form['pickup_time']
        
        success, message = transport_mgr.register_student_direct(student_id, student_name, route_number, route_name, driver_name, driver_phone, pickup_time)
        if success:
            transport_mgr.save_to_file()
            flash(message, 'success')
        else:
            flash(message, 'error')
    except ValueError:
        flash("Invalid input format!", 'error')
        
    return redirect(url_for('transport'))

@app.route('/transport/queue', methods=['POST'])
def add_transport_queue():
    try:
        student_id = int(request.form['student_id'])
        student_name = request.form['student_name']
        route_number = int(request.form['route_number'])
        request_date = request.form['request_date']
        
        success, message = transport_mgr.add_request_to_queue(student_id, student_name, route_number, request_date)
        if success:
            transport_mgr.save_queue_to_file()
            flash(message, 'success')
        else:
            flash(message, 'error')
    except ValueError:
        flash("Invalid input format!", 'error')
        
    return redirect(url_for('transport'))

@app.route('/transport/delete/<int:student_id>')
def delete_transport(student_id):
    transport_mgr.delete_node(student_id)
    transport_mgr.save_to_file()
    flash('Transport record deleted successfully!', 'success')
    return redirect(url_for('transport'))

if __name__ == '__main__':
    app.run(debug=True)
