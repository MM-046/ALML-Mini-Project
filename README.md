# Python Mini-Project: Classroom Practice Set

A collection of Python scripts designed to demonstrate core programming concepts, including data structures, conditional logic, loops, functions, and common algorithmic pitfalls.

##  Projects Included

### 1. Student Result Analyzer (`q1_result_analyzer.py`)
* **Difficulty:** Easy
* **Concepts:** Variables, Built-in Functions (`sum`, `len`, `enumerate`), Conditional Logic (`if-elif-else`), Loops.
* **Description:** Takes a student's basic details and a list of marks for 5 subjects. It calculates total and average marks, assigns an academic grade, and dynamically flags any specific subjects where the student scored below passing thresholds.

### 2. Library Book Management System (`q2_library_system.py`)
* **Difficulty:** Medium
* **Concepts:** Dictionaries, Tuples (Immutability), Lists, Sets (Uniqueness), Functions.
* **Description:** A mini library application that demonstrates choosing the *right data structure for the right job*. Uses an immutable tuple for book details, a fast-lookup dictionary for the catalog, a list to track borrowing history sequence, and a set to manage unique memberships cleanly.

### 3. Shopping Cart & Mutable Pitfalls (`q3_shopping_cart.py`)
* **Difficulty:** Hard / Concept-heavy
* **Concepts:** Default Parameters, Mutable vs. Immutable Types, Pass-by-Reference behavior.
* **Description:** Explores the dangerous Python pitfall of using mutable default arguments (like `cart=[]`). Includes a detailed code fix using `None` defaults, builds an independent shopping cart management system, and features a discussion section explaining object mutation vs. rebinding.

---

##  How to Run

Make sure you have Python 3 installed on your machine. You can execute any of the scripts directly from your terminal:

```bash
# Run Question 1
python q1_result_analyzer.py

# Run Question 2
python q2_library_system.py

# Run Question 3
python q3_shopping_cart.py
