"""The following code is used to check whether the string provided is palindrome or not through string slicing
method. """


def checkpalindrome(n):     # defining function
    rev = n[::-1]     # reversing the input string
    if n == rev:     # matching
        print("Congo! The input is palindrome.")
    else:
        print("Sorry! The input is not a palindrome")


# __main__
string = input("Enter a string to check palindrome.:")
checkpalindrome(string)
