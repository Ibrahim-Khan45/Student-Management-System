import os
import csv

class ExamRecord:
    def __init__(self, student_id, student_name, course_code, course_name, marks, grade):
        self.student_id = student_id
        self.student_name = student_name
        self.course_code = course_code
        self.course_name = course_name
        self.marks = marks
        self.grade = grade

class ExamManager:
    def __init__(self):
        self.records = [] # Using Python list as Dynamic Array
        self.count = 0

    def calculate_grade(self, marks):
        if marks >= 90: return 'A'
        elif marks >= 80: return 'B'
        elif marks >= 70: return 'C'
        elif marks >= 60: return 'D'
        else: return 'F'

    def create_exam_record(self, student_id, student_name, course_code, course_name, marks):
        if marks < 0 or marks > 100:
            return False, "Invalid marks! Must be between 0 and 100."
        
        grade = self.calculate_grade(marks)
        new_record = ExamRecord(student_id, student_name, course_code, course_name, marks, grade)
        self.records.append(new_record)
        self.count += 1
        return True, f"Exam record added successfully! Grade assigned: {grade}"

    def add_exam_record(self):
        print("\n--- Add Exam Record ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID format!")
            return

        student_name = input("Enter Student Name: ")
        course_code = input("Enter Course Code: ")
        course_name = input("Enter Course Name: ")
        
        try:
            marks = float(input("Enter Marks (0-100): "))
        except ValueError:
            print("Invalid marks format!")
            return

        success, message = self.create_exam_record(student_id, student_name, course_code, course_name, marks)
        print(f"\n{message}")
        if success:
             # Extract grade from message or just print message which already has it
             pass

    def display_all(self):
        if self.count == 0:
            print("\nNo exam records found!")
            return

        print("\n--- All Exam Records ---")
        print(f"{'Stu ID':<10}{'Student Name':<20}{'Course Code':<12}{'Course Name':<25}{'Marks':<8}{'Grade':<6}")
        print("-" * 85)

        for record in self.records:
            print(f"{record.student_id:<10}{record.student_name:<20}{record.course_code:<12}{record.course_name:<25}{record.marks:<8.2f}{record.grade:<6}")
        
        print(f"\nTotal Records: {self.count}")

    def search_by_student_id(self, student_id):
        # Linear Search
        for i, record in enumerate(self.records):
            if record.student_id == student_id:
                return i
        return -1

    def search_by_course(self, course_code):
        # Linear Search
        course_code = course_code.upper()
        for i, record in enumerate(self.records):
            if record.course_code.upper() == course_code:
                return i
        return -1

    def search_record(self):
        if self.count == 0:
            print("\nNo exam records found!")
            return

        print("\n--- Search Exam Record ---")
        print("1. Search by Student ID")
        print("2. Search by Course Code")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice!")
            return

        index = -1
        if choice == 1:
            try:
                student_id = int(input("Enter Student ID: "))
                index = self.search_by_student_id(student_id)
            except ValueError:
                print("Invalid ID!")
                return
        elif choice == 2:
            course_code = input("Enter Course Code: ")
            index = self.search_by_course(course_code)
        else:
            print("Invalid choice!")
            return

        if index != -1:
            record = self.records[index]
            print("\n--- Record Found ---")
            print(f"Student ID: {record.student_id}")
            print(f"Student Name: {record.student_name}")
            print(f"Course Code: {record.course_code}")
            print(f"Course Name: {record.course_name}")
            print(f"Marks: {record.marks}")
            print(f"Grade: {record.grade}")
        else:
            print("\nRecord not found!")

    def update_record(self):
        if self.count == 0:
            print("\nNo exam records found!")
            return

        print("\n--- Update Exam Record ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID!")
            return
        
        course_code = input("Enter Course Code: ")

        # Find the record
        index = -1
        for i, record in enumerate(self.records):
            if record.student_id == student_id and record.course_code.upper() == course_code.upper():
                index = i
                break
        
        if index == -1:
            print("Record not found!")
            return

        print(f"\nCurrent Marks: {self.records[index].marks}")
        try:
            new_marks = float(input("Enter new Marks (0-100): "))
            if new_marks < 0 or new_marks > 100:
                print("Invalid marks!")
                return
        except ValueError:
            print("Invalid marks format!")
            return

        self.records[index].marks = new_marks
        self.records[index].grade = self.calculate_grade(new_marks)

        print("\nRecord updated successfully!")
        print(f"New Grade: {self.records[index].grade}")

    def delete_record(self):
        if self.count == 0:
            print("\nNo exam records found!")
            return

        print("\n--- Delete Exam Record ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID!")
            return
        
        course_code = input("Enter Course Code: ")

        # Find the record
        index = -1
        for i, record in enumerate(self.records):
            if record.student_id == student_id and record.course_code.upper() == course_code.upper():
                index = i
                break
        
        if index == -1:
            print("Record not found!")
            return

        # Delete from list
        del self.records[index]
        self.count -= 1
        
        print("Record deleted successfully!")

    def sort_by_marks(self):
        # Selection Sort
        for i in range(self.count - 1):
            max_index = i
            for j in range(i + 1, self.count):
                if self.records[j].marks > self.records[max_index].marks:
                    max_index = j
            if max_index != i:
                self.records[i], self.records[max_index] = self.records[max_index], self.records[i]

    def sort_by_student_name(self):
        # Bubble Sort
        for i in range(self.count - 1):
            for j in range(self.count - i - 1):
                if self.records[j].student_name > self.records[j + 1].student_name:
                    self.records[j], self.records[j + 1] = self.records[j + 1], self.records[j]

    def sort_records(self):
        if self.count == 0:
            print("\nNo records to sort!")
            return

        print("\n--- Sort Records ---")
        print("1. Sort by Marks (Descending)")
        print("2. Sort by Student Name (Ascending)")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice!")
            return

        if choice == 1:
            self.sort_by_marks()
            print("Records sorted by marks!")
        elif choice == 2:
            self.sort_by_student_name()
            print("Records sorted by student name!")
        else:
            print("Invalid choice!")
            return

        self.display_all()

    def calculate_gpa(self, student_id):
        total_marks = 0.0
        course_count = 0
        
        for record in self.records:
            if record.student_id == student_id:
                total_marks += record.marks
                course_count += 1
        
        if course_count == 0:
            return 0.0
        
        average = total_marks / course_count
        if average >= 90: return 4.0
        elif average >= 80: return 3.5
        elif average >= 70: return 3.0
        elif average >= 60: return 2.5
        elif average >= 50: return 2.0
        else: return 1.0

    def calculate_student_gpa(self):
        if self.count == 0:
            print("\nNo exam records found!")
            return

        print("\n--- Calculate Student GPA ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID!")
            return

        gpa = self.calculate_gpa(student_id)
        total_marks = 0.0
        course_count = 0

        print(f"\n--- Exam Results for Student ID: {student_id} ---")
        print(f"{'Course Code':<12}{'Course Name':<25}{'Marks':<8}{'Grade':<6}")
        print("-" * 55)

        for record in self.records:
            if record.student_id == student_id:
                print(f"{record.course_code:<12}{record.course_name:<25}{record.marks:<8.2f}{record.grade:<6}")
                total_marks += record.marks
                course_count += 1
        
        if course_count > 0:
            average = total_marks / course_count
            print(f"\nAverage Marks: {average:.2f}")
            print(f"GPA: {gpa:.2f}/4.0")
        else:
            print("\nNo records found for this student!")

    def save_to_file(self):
        try:
            with open("exams.csv", "w", newline='') as file:
                writer = csv.writer(file)
                for record in self.records:
                    writer.writerow([record.student_id, record.student_name, record.course_code, record.course_name, record.marks, record.grade])
        except IOError as e:
            print(f"Error: Could not save to file! {e}")

    def load_from_file(self):
        if not os.path.exists("exams.csv"):
            return

        try:
            with open("exams.csv", "r", newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row:
                        continue
                    
                    if len(row) == 6:
                        student_id = int(row[0])
                        marks = float(row[4])
                        grade = row[5]
                        new_record = ExamRecord(student_id, row[1], row[2], row[3], marks, grade)
                        self.records.append(new_record)
                        self.count += 1
        except IOError:
            pass
        except ValueError:
            pass

    def menu(self):
        while True:
            print("\n--- Exam Record Management ---")
            print("1. Add Exam Record")
            print("2. Display All Records")
            print("3. Search Record")
            print("4. Update Record")
            print("5. Delete Record")
            print("6. Calculate Student GPA")
            print("7. Sort Records")
            print("8. Back to Main Menu")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice! Please try again.")
                continue

            if choice == 1:
                self.add_exam_record()
            elif choice == 2:
                self.display_all()
            elif choice == 3:
                self.search_record()
            elif choice == 4:
                self.update_record()
            elif choice == 5:
                self.delete_record()
            elif choice == 6:
                self.calculate_student_gpa()
            elif choice == 7:
                self.sort_records()
            elif choice == 8:
                self.save_to_file()
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice! Please try again.")
