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
                    
 print("write a python code to print factorial values by using both for anf while loops")
def factorial_for(n):
    if n<0:
        return "factorial is not defined for negative values"
    result=1
    for i in range(1,n+1):
        result*=i
    return result
num=int(input("Enter a non negative number to calculate its factorial:"))
print(f"Factorial of {num} using for loop is {factorial_for(num)}")                        

def factorial_while(n):
    if n<0:
        return "Factorial is not defined for negative values"
    result=1
    count=1
    while count<=n:
        result*=count
        count+=1
    return result
        
num=int(input("Enter a non negative number to print its factoeial:"))
print(f"factorial of {num} by using while loop is {factorial_while(num)}")

"""Create a python program that performss various on lists (such as adding,removing,sorting and revesing) 
and tuples(Accessing elements,slicing and unpacking)"""  
my_list=[10,20,30,40,50]
print("Original list:",my_list)
# Adding elements to the list
my_list.append(60)
print("After adding 60 to the list:",my_list)
# Removing elements from the list
my_list.remove(30)
print("after removing 30 from the list:",my_list)
# Sorting the list in ascending order
my_list.sort()
print("After sorting the list",my_list)
# Reversing the list
my_list.reverse()
print("After reversing the list:",my_list)
#Slicing the list
slice_list=my_list[1:4]#which print the list values from the index 
print("After slicing the list:",slice_list)

my_tuple=(100,200,350,400,550)
print("Original tuple:",my_tuple)
# Accessing elements in the tuple
print("First element in the tuple:",my_tuple[0])
# Slicing the tuple
slice_tuple=my_tuple[1:4]
print("After slicing the tuple from the index 1 to 3:",slice_tuple)
a,b,c,d,e=my_tuple
print("Unpacking the tuple:",a,b,c,d,e)
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)
print("e:",e)
         

"""Develop a python script that creates a dictionary to store and retrieve 
contact details(name and phone number)and demonstrate adding,updating and 
deleteing Entries"""
contact_book = {}

def add_contact(name, phone):
    if name in contact_book:
        print(f"Contact {name} already exists.")
    else:
        contact_book[name] = phone
        print(f"Contact {name} added successfully.")

def update_contact(name, phone):
    if name in contact_book:
        contact_book[name] = phone
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} is not found.")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} is deleted successfully.")
    else:
        print(f"Contact {name} is not found.")

def display_contacts():
    if contact_book:
        print("\nCurrent Contacts:")
        for name, phone in contact_book.items():
            print(f"Contact Name: {name} --- Contact Number: {phone}")
    else:
        print("No contacts found.")

# Main program execution
if __name__ == "__main__":
    add_contact("ADEEP", 9441182329)
    add_contact("TARUN", 7997557932)
    update_contact("TARUN", 9876543210)
    display_contacts()
    delete_contact("ADEEP")
    display_contacts()


"""Write a program that uses a while loop to find no. of vowels in given input string of lowercase latin letters.

Note: Vowels in lowercase latin letters are: a, e, i, o and u."""
input_1=input("Enter sring :")
vowels="aeiou"
vowel_c=0
index=0
while len(input_1)>index:
    if input_1[index] in vowels:
        vowel_c+=1
    index+=1
print(f"Number of vowels in given string is {vowel_c}") 
"""A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of N friends in Chefland want to buy Chef-TV subscriptions. We know that 
6 people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is 
X rupees. Determine the minimum total cost that the group of 
N friends will incur so that everyone in the group is able to use Chef-TV."""  
n,x=map(int,input().split())
numOfFrnds=n#here n is the number of friends willing to take subscription
costOfSub=x#Cost of subscription to cheftv
mincost=((n+5//6)*x)
print(mincost)


    

         


         
         
         

         
         
