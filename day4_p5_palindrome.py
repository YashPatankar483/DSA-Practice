# Problem Statement: Given an integer N, return true if it is a palindrome else return false.

def reverse_num(num):

    rev, rem = 0, 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    
    return rev

def is_palindrome(num):

    if num == reverse_num(num):
        return True
    
    return False

num = int(input("Enter any number: "))

print(is_palindrome(num))



