"""Develop a Student Record Management System using Python.

The program should:

Add student details.
Display all student records.
Search a student by name.
Delete a student record.
Use lists or dictionaries for data storage."""

students = []


# Function to add student

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "Name": name,
        "Roll Number": roll,
        "Branch": branch,
        "Marks": marks
    }

    students.append(student)

    print("\nStudent added successfully!")


# Function to display students

def display_students():
    if len(students) == 0:
        print("\nNo student records found.")
    else:
        print("\n----- Student Records -----")

        for student in students:
            print("Name:", student["Name"])
            print("Roll Number:", student["Roll Number"])
            print("Branch:", student["Branch"])
            print("Marks:", student["Marks"])
            print("---------------------------")


# Function to search student

def search_student():
    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["Name"].lower() == name.lower():
            print("\nStudent Found!")
            print(student)
            found = True

    if not found:
        print("Student not found.")


# Function to delete student

def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["Roll Number"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student record not found.")


# Main program

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")