"""Write a Python program that:

Creates a text file.
Writes your introduction into the file.
Reads and displays the file contents."""


file = open("introduction.txt", "w")

file.write("My name is Ratnesh Kumar.\n")
file.write("I am pursuing B.Tech.\n")
file.write("My branch is Artificial Intelligence and Data Science.\n")
file.write("I am interested in Data Science.")

file.close()

file = open("introduction.txt", "r")

print("File Contents:\n")
print(file.read())

file.close()