"""This is a small program to search any number among an array of numbers. This method is known as binary search. And
the code down below is based on iteration method. """


# Binary search iteration method.

def binary_search(ar, key):     # defining function
    low = 0
    high = len(ar) - 1
    while low <= high:      # while loop
        mid = int((low + high) / 2)
        if key == ar[mid]:
            return mid
        elif key < ar[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:       # to prevent unexpected error
        return -999


# creating an empty list
ar = []

# number of elements as input
n = int(input("Enter number of elements array should have : "))
print("Enter the numbers.")

# iterating till the range
for i in range(0, n):
    elem = int(input("Element " + str(i) + ":"))

    ar.append(elem)  # adding the element
ar.sort()  # sorting the list

print("Your input list is:", ar)
item = int(input("Enter a number to search:"))
search = binary_search(ar, item)
if search >= 0:
    print(item, "found at index", search)  # true output
else:
    print("Sorry!", item, "not found in the list")  # false output
