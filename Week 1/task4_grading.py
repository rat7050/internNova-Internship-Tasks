"""Write a Python program that:

Takes marks as input.
Displays the grade using if, elif, and else.

Example:

90+ → A
75–89 → B
60–74 → C
Below 60 → Fail"""

marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")

elif marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

else:
    print("Grade: Fail")