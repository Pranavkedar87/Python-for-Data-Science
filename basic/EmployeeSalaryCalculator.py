# Employee Salary Calculator

name = input("Enter Employee Name: ")
salary = float(input("Enter Basic Salary: "))

hra = salary * 0.20
da = salary * 0.10
gross = salary + hra + da

print("\n------ Salary Details ------")
print("Employee Name :", name)
print("Basic Salary  :", salary)
print("HRA           :", hra)
print("DA            :", da)
print("Gross Salary  :", gross)