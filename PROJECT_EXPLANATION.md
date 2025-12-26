# University Management System - Project Explanation

## 1. Project Overview
The **University Management System (UMS)** is a comprehensive application designed to manage key aspects of university administration. It handles **Student Records**, **Exam Results**, and **Transport Services**.

The project was originally conceived as a C++ console application and has been ported to **Python**, now featuring a modern **Web Interface** built with **Flask**.

## 2. System Architecture

### Frontend (User Interface)
-   **Technology**: HTML5, CSS3, Flask (Jinja2 Templates).
-   **Theme**: A custom "Black & Red" dark theme for a premium look.
-   **Interaction**: Users interact with the system via a web browser (Dashboard, Forms, Tables).

### Backend (Logic Layer)
-   **Technology**: Python 3.
-   **Design Pattern**: The system uses a modular approach where each component (Student, Exam, Transport) has its own Manager class.
-   **Separation of Concerns**: The core logic (adding, searching, sorting) is separated from the input/output layer, allowing both CLI and Web interfaces to use the same backend code.

### Data Persistence (Storage)
-   **Format**: CSV (Comma-Separated Values) files.
-   **Files**:
    -   `students.csv`: Stores student details.
    -   `exams.csv`: Stores exam marks and grades.
    -   `transport.csv`: Stores active transport registrations.
    -   `transport_queue.csv`: Stores pending transport requests.

## 3. Data Structures & Algorithms (DSA) Concepts

This project demonstrates the practical application of fundamental DSA concepts.

### A. Data Structures

#### 1. Singly Linked List
-   **Used In**: `StudentManager` (`student.py`) and `TransportManager` (`transport.py`).
-   **Concept**: A collection of nodes where each node contains data and a reference (pointer) to the next node.
-   **Why used here?**:
    -   **Dynamic Size**: We can add an infinite number of students/transport records without pre-allocating memory.
    -   **Efficient Insertion**: Adding a new record at the beginning is $O(1)$ (constant time).
-   **Implementation Details**:
    -   `StudentNode` / `TransportNode` classes represent the nodes.
    -   `head` pointer tracks the start of the list.

#### 2. Dynamic Array (Python List)
-   **Used In**: `ExamManager` (`exam.py`).
-   **Concept**: A contiguous block of memory that can resize itself. Python's built-in `list` is a dynamic array.
-   **Why used here?**:
    -   **Fast Access**: We can access any exam record instantly by index ($O(1)$).
    -   **Cache Friendliness**: Elements are stored next to each other in memory.

#### 3. Queue (FIFO - First In, First Out)
-   **Used In**: `TransportManager` (`transport.py`).
-   **Concept**: A linear structure where elements are added at one end (rear) and removed from the other (front).
-   **Why used here?**:
    -   **Fairness**: Transport requests are processed in the order they are received. The first student to request gets priority.
-   **Implementation**: Python's `collections.deque` is used for efficient append and pop operations.

### B. Algorithms

#### 1. Sorting Algorithms
Sorting is used to organize records for better readability.

-   **Bubble Sort**:
    -   **Used For**: Sorting Students by ID or Name (`student.py`), Sorting Exams by Student Name (`exam.py`).
    -   **Mechanism**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    -   **Time Complexity**: $O(n^2)$ (Quadratic) - Simple to implement but inefficient for very large datasets.

-   **Selection Sort**:
    -   **Used For**: Sorting Exams by Marks (`exam.py`).
    -   **Mechanism**: Repeatedly finds the minimum/maximum element from the unsorted part and puts it at the beginning.
    -   **Time Complexity**: $O(n^2)$ (Quadratic).

#### 2. Searching Algorithms
Searching is used to find specific records.

-   **Linear Search**:
    -   **Used For**: Finding a student by ID, finding an exam record, checking if a student is already registered.
    -   **Mechanism**: Iterates through the list/array one by one from the beginning until the target is found.
    -   **Time Complexity**: $O(n)$ (Linear) - The time taken grows linearly with the number of records.

## 4. Key Files Guide

| File | Description |
| :--- | :--- |
| `app.py` | **Main Entry Point**. The Flask web server application. Defines routes (URLs) and connects the web UI to the backend managers. |
| `student.py` | Contains `StudentNode` and `StudentManager`. Implements Linked List logic for students. |
| `exam.py` | Contains `ExamRecord` and `ExamManager`. Implements Dynamic Array logic for exams. |
| `transport.py` | Contains `TransportNode`, `TransportRequest`, and `TransportManager`. Implements Linked List and Queue logic. |
| `templates/` | Directory containing HTML files (`index.html`, `students.html`, etc.) for the web interface. |
| `static/css/` | Directory containing `style.css` for the Black & Red theme. |

## 5. How to Run
1.  Ensure Python is installed.
2.  Install Flask: `pip install flask`
3.  Run the application: `python app.py`
4.  Open your browser and visit: `http://127.0.0.1:5000`
