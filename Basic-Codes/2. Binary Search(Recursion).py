"""This is a small program to search any number among an array of numbers. This is generally known as binary search
method. And the code down below is based on recursion method. """


# Binary search recursion method.

def binary_search(ar, key, low, high):  # defining function
    if low > high:
        return -999  # to prevent unexpected error
    mid = int((low + high) / 2)
    if key == ar[mid]:
        return mid
    elif key < ar[mid]:
        high = mid - 1
        return binary_search(ar, key, low, high)  # recursion
    else:
        low = mid + 1
        return binary_search(ar, key, low, high)  # recursion

    # main program

    # creating an empty list
    ar = []

    # number of elements as input
    n = int(input("Enter number of elements : "))
    print("Enter the numbers.")

    # iterating till the range
    for i in range(0, n):
        ele = int(input("Element " + str(i) + ":"))

        ar.append(ele)  # adding the element
    ar.sort()  # sorting the list

    print("Your input list is:", ar)
    item = int(input("Enter a number to search:"))
    search = binary_search(ar, item, 0, len(ar) - 1)
    if search >= 0:
        print(item, "found at index", search)  # true output
    else:
        print("Sorry!", item, "not found in the list")  # false output
