# Create programs to demonstrate:

# String operations (upper(), lower(), replace(), find())

text = "Python Programming"

print("Original String:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Python", "Java"))
print("Find:", text.find("Programming"))

# List operations (append(), remove(), sort())

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

fruits.append("Orange")
print("After Append:", fruits)

fruits.remove("Banana")
print("After Remove:", fruits)

fruits.sort()
print("After Sort:", fruits)

# Tuple creation and indexing

students = ("Ratnesh", "Rahul", "Aman", "Rohit")

print("Student Tuple:", students)

print("First Student:", students[0])
print("Second Student:", students[1])
print("Last Student:", students[-1])

# Dictionary storing student information

student = {
    "Name": "Ratnesh Kumar",
    "College": "SIRT Excellence",
    "Branch": "AI & Data Science",
    "Age": 21
}

print("Student Information:")

print(student)

# Set operations (add(), remove())

numbers = {10, 20, 30, 40}

print("Original Set:", numbers)

numbers.add(50)
print("After Add:", numbers)

numbers.remove(20)
print("After Remove:", numbers)