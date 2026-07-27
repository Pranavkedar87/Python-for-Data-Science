# Student Grade Management System

students = []

num_students = 5

for i in range(num_students):
    print(f"\nEnter details for Student {i + 1}")

    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")

    mark1 = float(input("Enter Marks for Subject 1: "))
    mark2 = float(input("Enter Marks for Subject 2: "))
    mark3 = float(input("Enter Marks for Subject 3: "))

    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    student = {
        "Name": name,
        "Roll": roll,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

    students.append(student)

# Display Student Records
print("\n" + "-" * 70)
print(f"{'Name':<15}{'Roll':<10}{'Total':<10}{'Average':<12}{'Grade':<8}")
print("-" * 70)

for student in students:
    print(f"{student['Name']:<15}{student['Roll']:<10}"
          f"{student['Total']:<10.2f}"
          f"{student['Average']:<12.2f}"
          f"{student['Grade']:<8}")

# Find Topper and Lowest Average
topper = students[0]
lowest = students[0]

passed = 0
failed = 0

for student in students:
    if student["Average"] > topper["Average"]:
        topper = student

    if student["Average"] < lowest["Average"]:
        lowest = student

    if student["Average"] >= 40:
        passed += 1
    else:
        failed += 1

print("-" * 70)
print(f"Topper           : {topper['Name']} ({topper['Average']:.2f}%)")
print(f"Lowest Average   : {lowest['Name']} ({lowest['Average']:.2f}%)")
print(f"Passed Students  : {passed}")
print(f"Failed Students  : {failed}")