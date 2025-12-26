import os
import csv

class StudentNode:
    def __init__(self, student_id, name, department, phone, email):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.phone_number = phone
        self.email = email
        self.next = None

class StudentManager:
    def __init__(self):
        self.head = None
        self.count = 0

    def search_by_id(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                return current
            current = current.next
        return None

    def search_by_name(self, name):
        current = self.head
        name = name.lower()
        while current:
            if name in current.name.lower():
                return current
            current = current.next
        return None

    def delete_node(self, student_id):
        if not self.head:
            return

        if self.head.student_id == student_id:
            self.head = self.head.next
            self.count -= 1
            return

        current = self.head
        while current.next:
            if current.next.student_id == student_id:
                current.next = current.next.next
                self.count -= 1
                return
            current = current.next

    def sort_by_id(self):
        # Bubble Sort for Linked List
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.student_id > current.next.student_id:
                    # Swap data
                    current.student_id, current.next.student_id = current.next.student_id, current.student_id
                    current.name, current.next.name = current.next.name, current.name
                    current.department, current.next.department = current.next.department, current.department
                    current.phone_number, current.next.phone_number = current.next.phone_number, current.phone_number
                    current.email, current.next.email = current.next.email, current.email
                    swapped = True
                current = current.next

    def sort_by_name(self):
        # Bubble Sort for Linked List by Name
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.name > current.next.name:
                    # Swap data
                    current.student_id, current.next.student_id = current.next.student_id, current.student_id
                    current.name, current.next.name = current.next.name, current.name
                    current.department, current.next.department = current.next.department, current.department
                    current.phone_number, current.next.phone_number = current.next.phone_number, current.phone_number
                    current.email, current.next.email = current.next.email, current.email
                    swapped = True
                current = current.next

    def create_student(self, student_id, name, department, phone, email):
        if self.search_by_id(student_id):
            return False, "Error: Student ID already exists!"

        # Insert at beginning (O(1))
        new_node = StudentNode(student_id, name, department, phone, email)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True, "Student record added successfully!"

    def add_student(self):
        print("\n--- Add New Student ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID format!")
            return

        name = input("Enter Name: ")
        department = input("Enter Department: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        success, message = self.create_student(student_id, name, department, phone, email)
        print(message)

    def display_all(self):
        if not self.head:
            print("\nNo student records found!")
            return

        self.sort_by_id()

        print("\n--- All Student Records ---")
        print(f"{'ID':<10}{'Name':<25}{'Department':<20}{'Phone':<15}{'Email':<30}")
        print("-" * 100)

        current = self.head
        while current:
            print(f"{current.student_id:<10}{current.name:<25}{current.department:<20}{current.phone_number:<15}{current.email:<30}")
            current = current.next
        
        print(f"\nTotal Records: {self.count}")

    def search_student(self):
        if not self.head:
            print("\nNo student records found!")
            return

        print("\n--- Search Student ---")
        print("1. Search by ID")
        print("2. Search by Name")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice!")
            return

        found = None
        if choice == 1:
            try:
                student_id = int(input("Enter Student ID: "))
                found = self.search_by_id(student_id)
            except ValueError:
                print("Invalid ID!")
                return
        elif choice == 2:
            name = input("Enter Student Name: ")
            found = self.search_by_name(name)
        else:
            print("Invalid choice!")
            return

        if found:
            print("\n--- Student Found ---")
            print(f"ID: {found.student_id}")
            print(f"Name: {found.name}")
            print(f"Department: {found.department}")
            print(f"Phone: {found.phone_number}")
            print(f"Email: {found.email}")
        else:
            print("\nStudent not found!")

    def update_student(self):
        if not self.head:
            print("\nNo student records found!")
            return

        print("\n--- Update Student ---")
        try:
            student_id = int(input("Enter Student ID to update: "))
        except ValueError:
            print("Invalid ID!")
            return

        found = self.search_by_id(student_id)
        if not found:
            print("Student not found!")
            return

        print("\nCurrent Details:")
        print(f"Name: {found.name}")
        print(f"Department: {found.department}")
        print(f"Phone: {found.phone_number}")
        print(f"Email: {found.email}")

        print("\nWhat would you like to update?")
        print("1. Department")
        print("2. Phone Number")
        print("3. Email")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice!")
            return

        if choice == 1:
            found.department = input("Enter new Department: ")
        elif choice == 2:
            found.phone_number = input("Enter new Phone Number: ")
        elif choice == 3:
            found.email = input("Enter new Email: ")
        else:
            print("Invalid choice!")
            return

        print("\nStudent record updated successfully!")

    def delete_student(self):
        if not self.head:
            print("\nNo student records found!")
            return

        print("\n--- Delete Student ---")
        try:
            student_id = int(input("Enter Student ID to delete: "))
        except ValueError:
            print("Invalid ID!")
            return

        found = self.search_by_id(student_id)
        if not found:
            print("Student not found!")
            return

        print(f"\nDeleting student: {found.name} (ID: {found.student_id})")
        self.delete_node(student_id)
        print("Student record deleted successfully!")

    def save_to_file(self):
        try:
            with open("students.csv", "w", newline='') as file:
                writer = csv.writer(file)
                current = self.head
                while current:
                    writer.writerow([current.student_id, current.name, current.department, current.phone_number, current.email])
                    current = current.next
        except IOError as e:
            print(f"Error: Could not save to file! {e}")

    def load_from_file(self):
        if not os.path.exists("students.csv"):
            return

        try:
            with open("students.csv", "r", newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row:
                        continue
                    
                    if len(row) == 5:
                        student_id = int(row[0])
                        new_node = StudentNode(student_id, row[1], row[2], row[3], row[4])
                        new_node.next = self.head
                        self.head = new_node
                        self.count += 1
        except IOError:
            pass
        except ValueError:
            pass # Skip malformed lines

    def menu(self):
        while True:
            print("\n--- Student Record Management ---")
            print("1. Add New Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Update Student Details")
            print("5. Delete Student")
            print("6. Back to Main Menu")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice! Please try again.")
                continue

            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.display_all()
            elif choice == 3:
                self.search_student()
            elif choice == 4:
                self.update_student()
            elif choice == 5:
                self.delete_student()
            elif choice == 6:
                self.save_to_file()
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice! Please try again.")
