#Recurion Function
#Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem.
# Each recursive call works on a smaller part of the problem until a base condition is met, which stops the recursion.
print("Factorial is a example for recursion")

def factorial(n):# Base case: if n is 0 or 1, return 1
    if n==1:
        return 1
    else:
        return n* factorial(n-1) # Recursive case: call factorial with n-1
    
print(factorial(5))

def fibonacci_recursive(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)  # Recursive case

# Print the first 10 Fibonacci numbers
for i in range(20):
    print(fibonacci_recursive(i), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34

print("Printing the Fibonacci series in the another way")    
print("\n\t")
n=int(input("Enter the nth range:"))  
a=0
b=1
lst=[a,b]
for i in range(n):
    sum=a+b
    a=b
    b=sum
    lst.append(sum)
print(*lst)    

print("Example of recursion in sum natural number")
def sum_Natural(n):
    if n==0:
        return 0
    else:
        return n+sum_Natural(n-1)
    
sum=sum_Natural(10)
print(sum)   

print("Example of recursion to power of the number") 
def power(x,y):
    if y==0:
        return 1
    return x*power(x,y-1)

num=power(2,6)#here the recursive function x^y  
print(num)
    
print("Example for the recursion to reverse the string") 
def revers_string(s):
    if len(s)==0:
        return s
    return s[-1]+revers_string(s[:-1])

input_string=input("Enter the string to reverse:") 
reverse_result=revers_string(input_string)
print(f"The original string ={input_string}")   
print(f"The reversed result={reverse_result}")       
    
     
    
        
            
        
    
        
            
    