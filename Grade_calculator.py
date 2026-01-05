# Student Grade Calculator
# Author: Your Name
# Description: Simple program to calculate grade based on marks

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

print("---- Student Grade Calculator ----")

name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(subjects):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total += marks

average = total / subjects
grade = calculate_grade(average)

print("\n---- Result ----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
