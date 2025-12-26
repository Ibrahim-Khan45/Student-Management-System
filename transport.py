import os
import csv
from collections import deque

class TransportNode:
    def __init__(self, student_id, student_name, route_number, route_name, driver_name, driver_phone, pickup_time):
        self.student_id = student_id
        self.student_name = student_name
        self.route_number = route_number
        self.route_name = route_name
        self.driver_name = driver_name
        self.driver_phone = driver_phone
        self.pickup_time = pickup_time
        self.next = None

class TransportRequest:
    def __init__(self, student_id, student_name, preferred_route, request_date):
        self.student_id = student_id
        self.student_name = student_name
        self.preferred_route = preferred_route
        self.request_date = request_date

class TransportManager:
    def __init__(self):
        self.head = None
        self.request_queue = deque() # Using deque as Queue
        self.count = 0
        self.load_queue_from_file()

    def search_by_student_id(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                return current
            current = current.next
        return None

    def search_by_route(self, route_number):
        current = self.head
        while current:
            if current.route_number == route_number:
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

    def register_student_direct(self, student_id, student_name, route_number, route_name, driver_name, driver_phone, pickup_time):
        if self.search_by_student_id(student_id):
            return False, "Error: Student already registered for transport!"

        new_node = TransportNode(student_id, student_name, route_number, route_name, driver_name, driver_phone, pickup_time)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True, "Student registered successfully!"

    def add_request_to_queue(self, student_id, student_name, route_number, request_date):
        request = TransportRequest(student_id, student_name, route_number, request_date)
        self.request_queue.append(request)
        return True, "Request added to queue. It will be processed later."

    def register_student(self):
        print("\n--- Register Student for Transport ---")
        print("1. Direct Registration")
        print("2. Add to Request Queue")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice!")
            return

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID!")
            return
            
        student_name = input("Enter Student Name: ")
        try:
            route_number = int(input("Enter Route Number: "))
        except ValueError:
            print("Invalid Route Number!")
            return

        if choice == 1:
            # Direct registration
            route_name = input("Enter Route Name: ")
            driver_name = input("Enter Driver Name: ")
            driver_phone = input("Enter Driver Phone: ")
            pickup_time = input("Enter Pickup Time (e.g., 7:30 AM): ")

            success, message = self.register_student_direct(student_id, student_name, route_number, route_name, driver_name, driver_phone, pickup_time)
            print(f"\n{message}")
        else:
            # Add to queue
            request_date = input("Enter Request Date (DD/MM/YYYY): ")
            success, message = self.add_request_to_queue(student_id, student_name, route_number, request_date)
            print(f"\n{message}")

    def process_request(self):
        if not self.request_queue:
            print("\nNo pending requests in queue!")
            return

        request = self.request_queue.popleft()

        print("\n--- Processing Request ---")
        print(f"Student ID: {request.student_id}")
        print(f"Student Name: {request.student_name}")
        print(f"Preferred Route: {request.preferred_route}")
        print(f"Request Date: {request.request_date}")

        if self.search_by_student_id(request.student_id):
            print("Error: Student already registered!")
            self.save_queue_to_file()
            return

        route_name = input("\nEnter Route Name: ")
        driver_name = input("Enter Driver Name: ")
        driver_phone = input("Enter Driver Phone: ")
        pickup_time = input("Enter Pickup Time (e.g., 7:30 AM): ")

        new_node = TransportNode(request.student_id, request.student_name, request.preferred_route, route_name, driver_name, driver_phone, pickup_time)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

        self.save_queue_to_file()
        print("\nRequest processed and student registered successfully!")

    def display_all(self):
        if not self.head:
            print("\nNo transport records found!")
            return

        print("\n--- All Transport Records ---")
        print(f"{'Stu ID':<10}{'Student Name':<20}{'Route':<8}{'Route Name':<20}{'Driver Name':<20}{'Driver Phone':<15}{'Pickup Time':<12}")
        print("-" * 105)

        current = self.head
        while current:
            print(f"{current.student_id:<10}{current.student_name:<20}{current.route_number:<8}{current.route_name:<20}{current.driver_name:<20}{current.driver_phone:<15}{current.pickup_time:<12}")
            current = current.next
        
        print(f"\nTotal Records: {self.count}")

    def search_record(self):
        if not self.head:
            print("\nNo transport records found!")
            return

        print("\n--- Search Transport Record ---")
        print("1. Search by Student ID")
        print("2. Search by Route Number")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice!")
            return

        found = None
        if choice == 1:
            try:
                student_id = int(input("Enter Student ID: "))
                found = self.search_by_student_id(student_id)
            except ValueError:
                print("Invalid ID!")
                return
        elif choice == 2:
            try:
                route_number = int(input("Enter Route Number: "))
                found = self.search_by_route(route_number)
            except ValueError:
                print("Invalid Route Number!")
                return
        else:
            print("Invalid choice!")
            return

        if found:
            print("\n--- Record Found ---")
            print(f"Student ID: {found.student_id}")
            print(f"Student Name: {found.student_name}")
            print(f"Route Number: {found.route_number}")
            print(f"Route Name: {found.route_name}")
            print(f"Driver Name: {found.driver_name}")
            print(f"Driver Phone: {found.driver_phone}")
            print(f"Pickup Time: {found.pickup_time}")
        else:
            print("\nRecord not found!")

    def update_record(self):
        if not self.head:
            print("\nNo transport records found!")
            return

        print("\n--- Update Transport Record ---")
        try:
            student_id = int(input("Enter Student ID to update: "))
        except ValueError:
            print("Invalid ID!")
            return

        found = self.search_by_student_id(student_id)
        if not found:
            print("Record not found!")
            return

        print("\nCurrent Details:")
        print(f"Route Number: {found.route_number}")
        print(f"Route Name: {found.route_name}")
        print(f"Driver Name: {found.driver_name}")
        print(f"Driver Phone: {found.driver_phone}")
        print(f"Pickup Time: {found.pickup_time}")

        print("\nWhat would you like to update?")
        print("1. Route Number & Name")
        print("2. Driver Name & Phone")
        print("3. Pickup Time")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice!")
            return

        if choice == 1:
            try:
                found.route_number = int(input("Enter new Route Number: "))
            except ValueError:
                print("Invalid Route Number!")
                return
            found.route_name = input("Enter new Route Name: ")
        elif choice == 2:
            found.driver_name = input("Enter new Driver Name: ")
            found.driver_phone = input("Enter new Driver Phone: ")
        elif choice == 3:
            found.pickup_time = input("Enter new Pickup Time: ")
        else:
            print("Invalid choice!")
            return

        print("\nRecord updated successfully!")

    def remove_student(self):
        if not self.head:
            print("\nNo transport records found!")
            return

        print("\n--- Remove Student from Transport ---")
        try:
            student_id = int(input("Enter Student ID to remove: "))
        except ValueError:
            print("Invalid ID!")
            return

        found = self.search_by_student_id(student_id)
        if not found:
            print("Record not found!")
            return

        print(f"\nRemoving student: {found.student_name} (ID: {found.student_id})")
        self.delete_node(student_id)
        print("Student removed from transport successfully!")

    def display_pending_requests(self):
        if not self.request_queue:
            print("\nNo pending requests!")
            return

        print("\n--- Pending Transport Requests (Queue) ---")
        print(f"{'Stu ID':<10}{'Student Name':<20}{'Route':<8}{'Request Date':<15}")
        print("-" * 55)

        for req in self.request_queue:
            print(f"{req.student_id:<10}{req.student_name:<20}{req.preferred_route:<8}{req.request_date:<15}")
        
        print(f"\nTotal Pending Requests: {len(self.request_queue)}")

    def save_to_file(self):
        try:
            with open("transport.csv", "w", newline='') as file:
                writer = csv.writer(file)
                current = self.head
                while current:
                    writer.writerow([current.student_id, current.student_name, current.route_number, current.route_name, current.driver_name, current.driver_phone, current.pickup_time])
                    current = current.next
        except IOError as e:
            print(f"Error: Could not save to file! {e}")

    def load_from_file(self):
        if not os.path.exists("transport.csv"):
            return

        try:
            with open("transport.csv", "r", newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row:
                        continue
                    
                    if len(row) == 7:
                        student_id = int(row[0])
                        route_number = int(row[2])
                        new_node = TransportNode(student_id, row[1], route_number, row[3], row[4], row[5], row[6])
                        new_node.next = self.head
                        self.head = new_node
                        self.count += 1
        except IOError:
            pass
        except ValueError:
            pass

    def save_queue_to_file(self):
        try:
            with open("transport_queue.csv", "w", newline='') as file:
                writer = csv.writer(file)
                for req in self.request_queue:
                    writer.writerow([req.student_id, req.student_name, req.preferred_route, req.request_date])
        except IOError:
            pass

    def load_queue_from_file(self):
        if not os.path.exists("transport_queue.csv"):
            return

        try:
            with open("transport_queue.csv", "r", newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row:
                        continue
                    
                    if len(row) == 4:
                        student_id = int(row[0])
                        preferred_route = int(row[2])
                        request = TransportRequest(student_id, row[1], preferred_route, row[3])
                        self.request_queue.append(request)
        except IOError:
            pass
        except ValueError:
            pass

    def menu(self):
        while True:
            print("\n--- Transport Record Management ---")
            print("1. Register Student for Transport")
            print("2. Process Request from Queue")
            print("3. Display All Records")
            print("4. Search Record")
            print("5. Update Record")
            print("6. Remove Student")
            print("7. Display Pending Requests")
            print("8. Back to Main Menu")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice! Please try again.")
                continue

            if choice == 1:
                self.register_student()
            elif choice == 2:
                self.process_request()
            elif choice == 3:
                self.display_all()
            elif choice == 4:
                self.search_record()
            elif choice == 5:
                self.update_record()
            elif choice == 6:
                self.remove_student()
            elif choice == 7:
                self.display_pending_requests()
            elif choice == 8:
                self.save_to_file()
                self.save_queue_to_file()
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice! Please try again.")
