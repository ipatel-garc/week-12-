# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


# Practice Problems:
#score / grade calculator
# if the score is between 90 and 100 inclusive, print A
# if the score is between 80 and 89 inclusive, print B
# if the score is between 70 and 79 inclusive, print C
# if the score is below a 70, print F

score = int(input("What is your score?:"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 100:
    print("C")
elif 60 <= score <= 69:
    print("D")
else score< 60:
    print("F")


# Write an expression that checks if a number is between 50 and 100 (inclusive).
number = int(input("Insert your number:"))
if 50<= number<= 100:
    print("Your number is included.")
else:
    print("")

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:

