list = []
n = int(input("Enter the no of student:"))
for i in range(0,n):
    list.append(int(input(f"Enter the {i+1}:")))

def avg(list):
    return sum(list)/len(list)

def Min(list):
    return min(list)

def Max(list):
    return max(list)

print("The avg of marks:",avg(list))
print("The minmium of student:",Min(list))
print("The maximum of student:",Max(list))
