import sys
from student import StudentManager
from exam import ExamManager
from transport import TransportManager

def display_main_menu():
    print("\n========================================")
    print("   UNIVERSITY MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Student Record Management")
    print("2. Exam Record Management")
    print("3. Transport Record Management")
    print("4. Exit")
    print("========================================")

def main():
    student_mgr = StudentManager()
    exam_mgr = ExamManager()
    transport_mgr = TransportManager()

    # Load existing data from files
    student_mgr.load_from_file()
    exam_mgr.load_from_file()
    transport_mgr.load_from_file()

    while True:
        display_main_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid choice! Please try again.")
            continue

        if choice == 1:
            student_mgr.menu()
        elif choice == 2:
            exam_mgr.menu()
        elif choice == 3:
            transport_mgr.menu()
        elif choice == 4:
            # Save all data before exiting
            student_mgr.save_to_file()
            exam_mgr.save_to_file()
            transport_mgr.save_to_file()
            transport_mgr.save_queue_to_file()
            print("\nAll data saved successfully!")
            print("Thank you for using University Management System!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
