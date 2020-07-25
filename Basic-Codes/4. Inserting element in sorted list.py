"""Inserting elements in a sorted list """
# let a pre sorted list(my method)

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The pre sorted list is", mylist)
new = int(input("Enter the element to insert in the list:"))
mylist.append(new)
mylist.sort()
print(new, "is inserted at index", mylist.index(new))
print("The updated list is:", mylist)

