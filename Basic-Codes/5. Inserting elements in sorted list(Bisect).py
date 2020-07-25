"""Inserting elements in a sorted list using bisect module."""

# importing bisect
import bisect

mylist = [10, 20, 30, 40, 50, 60, 70, 800, 90, 100]
print("The list in sorted order is:", mylist)
item = int(input("Enter new element to be inserted:"))
ind = bisect.bisect(mylist, item)
bisect.insort(mylist, item)
print(item, "inserted at index", ind)
print("The list after inserting new element is:", mylist)
