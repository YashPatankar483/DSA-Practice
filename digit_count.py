# Problem Statement:  Given an integer N, return the number of digits in N.

import math

num = int(input("Enter any number: "))
# count = 0

# while num != 0:
#     num = num // 10
#     count += 1

# Optimal approach
count = int(math.log10(num) + 1)

print(count)

"""
log10N means what power of 10 gives that number N.
So here the observation is, the place value of any digit is a multiple of 10. So for any number suppose 235, the place value
of 2 is 100 i.e power of 2. This value is what we get from the log (approx since the value can also be in decimals). So we add 1
to it. This gives the actual number of digits in the number. 
"""