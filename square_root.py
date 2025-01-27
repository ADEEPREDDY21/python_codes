# in python we can write code for finding square root of any integers
import math
#by importing math library to perform any math related operations
number=int(input("Enter number to check its square root number:")
square_root=math.sqrt(n)
print(f"Square root of {number} is {square_root:.5f}")

#another way to run a code for square root of any number
number=int(input("Enter any integer number to check it's square root"))
squareRoot=number**0.5
print(f"Square root of {number} is {squareRoot:.4f}")
           
#we can also round the decimal point by using round key word
number=int(input("Enter any number to check it's square root number:"))
squareRoot=round(number**0.5)
print(f"Square root of {number} is {squareRoot}")
             
