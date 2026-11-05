# Write Python programs to:
# Print numbers from 1 to 20 using a for loop.

for i in range(1, 21):
    print(i)

# Print the multiplication table of any number.

num = int(input("Enter a number: "))

print("Multiplication Table of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Print even numbers from 1 to 50 using a while loop.

num = 2

while num <= 50:
    print(num)
    num += 2