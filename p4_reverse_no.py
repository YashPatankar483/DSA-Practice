# Problem Statement: Given an integer N return the reverse of the given number.

num = int(input("Enter any number: "))
rev_num = 0

while num != 0:

    rev_num = (10 * rev_num) + (num % 10)
    num //= 10

print(rev_num) 