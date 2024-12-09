#print("PRINT the Second Largest number")
def second_max(a,b,c):
    if (a>b and a<c) or (a>c and a<b):
        return a

    elif (b>a and b<c)or (b>c and b<a):
        return b
    else:
        return c

a,b,c=map(int,input("enter a , b , c values:").split())
second_high=second_max(a,b,c)
print(second_high)

print("To print gcd of 2 number")
def gcd(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return abs(num1)
num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))
GCD=gcd(num1,num2)
print(GCD)
print("ANOTHER way to print gcd of two numbers")
import math
num1=int(input("Enter number 1:")
num2=int(input("Enter number 2:")
print(math.gcd(num1,num2))

print("Set Username and Password")
def set_details():
    print("Set your sign in details")
    user_name=input("Enter USER NAME:")
    while True:
        password=input("Enter Your password:")
        confirm_password=input("Re-enter your password:")
        if password==confirm_password:
            print("User Name and Password is set Successfully")
            return user_name,password
        else:
            print("Password and Confirm password is mismatch")    

def verify_pass(stored_user,stored_pass):
    user_name=input("Enter username:")            
    password=input("Enter Your password:")
    if user_name==stored_user and password==stored_pass:
        print("Login Successfully..!")
    else:
        print("Invalid Username or Password")    

def main():
    stored_user,stored_pass=set_details()
    verify_pass(stored_user,stored_pass)
if __name__=="__main__":
    main()         

print("Sum of total numbers given")
n=int(input("Enter the number to give output as sum of each number:"))
print(sum(int(digit) for digit in str(n)))
print("Another way to print the sum of each number ")
n=int(input("Enter the number to give output as sum of each number:"))
sumof=0
while n>0:
    sumof +=n%10
    n//=10
print(sumof)   
         
         


         


         
         
         

         
         
