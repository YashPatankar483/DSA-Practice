# Problem Statement: Given two numbers find their GCD

def gcd(num1, num2):

    if num1 == num2:
        return num1
    
    div = num1 if (num2 > num1) else num2

    while div > 0:
        
        if (num1 % div == 0) and (num2 % div == 0):
            return div
        
        div -= 1
        
    return div
    
    

num1 = int(input('Enter any number: '))
num2 = int(input('Enter any number: '))

print(f'The GCD of two given numbers {num1} and {num2} is: {gcd(num1, num2)}')





