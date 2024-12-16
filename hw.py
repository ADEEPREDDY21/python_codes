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
"""
if yoy bought car insurance. The policy of the insurance is:

The maximum rebatable amount for any damage is Rs 
X
X lakhs.
If the amount required for repairing the damage is ≤X lakhs, that amount is rebated in full.
Chef's car meets an accident and required Rs 
Y
Y lakhs for repairing.

Determine the amount that will be rebated by the insurance company."""


for r in range(int(input())):
    x,y=map(int,input().split())
    print(min(x,y))
"""Chef and Gym
Chef has decided to join a Gym in ChefLand and if possible, also hire a personal trainer at the gym. The monthly cost of the gym is 
X
X and personal training will cost him an additional 
Y
Y per month. Chef's total budget per month is only 
Z
Z. Print 1 if Chef can only join the gym, 2 if he can also have a personal trainer, and 0 if he can't even join the gym.

Note that if Chef wants to hire a personal trainer, he must join the gym — he cannot hire the trainer without joining the gym.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases. Then the test cases follow.
Each test case consists of a single line of input containing three space-separated integers 
X
,
Y
,
Z
X,Y,Z.
Output Format
For each test case, output in a single line 2 if Chef can go to the gym and have a trainer, 1 if Chef can only go to the gym, 0 if he can't even go to the gym."""
def gym_trainer(x,y,z):
    if x+y<=z:
        return 2
    elif x<=z:
        return 1
    else:
        return 0
t=int(input())
for r in range(t):
    x,y,z=map(int,input().split())
    print(gym_trainer(x,y,z))    
                    
         
         


         


         
         
         

         
         
