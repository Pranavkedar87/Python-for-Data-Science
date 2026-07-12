l1 = []
n = int(input("Enter size of list: "))
for i in range(0,n):
    #appen function add the elemnt at last
    l1.append(int(input(f"Enter the {i+1} elemnt: ")))
print(l1) 
#sort 
l1.sort()
print(l1)
#reverse the list
l1.reverse()
print(l1)
#insert at specific position
l1.insert(2,1)
print(l1)
#pop and return the element
print(l1.pop(1))
#remove the element
l1.remove(2)
print(l1)