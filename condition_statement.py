"""In Python, control statements manage the flow of execution in a program. 
They allow you to make decisions, repeat tasks, or control when specific blocks 
of code are executed. The main types of control statements are:"""
#control statements are classified into three types
'''they are
1,selection or conditional statement
2,sequence
3,iteration or looping'''
#selection control statements
#seleection control statements are usually knows as These are used to execute code based on certain conditions.
'''1,if-->do or dont
   2,elif--> based on the true or false of condition do this or otherwise do that
   3,else-->based on the true or false of given condition choose one from many
   4,nested if -->if condition is true then check the next condition'''                
print("Example of if Statement")
order=int(input("Enter order price:"))
minimum_price=500
delivery=50
total_price=order+delivery

if order > minimum_price:
   delivery=0
total_price=order+delivery
print(f"{total_price} is your order price")#here space before print statement is known as indentation which is required in pyhton

print("Check Whether given number is even or not")
num=int(input("Enter a number Which want to check"))
if num%2==0:
   print(f"{num} is an even number")
else:
   print(f"{num} is not an event number")   
   
print("Checking username and password by if else statement")   
username=input("Enter user name:")
password=input("Enter your password:")

if username=="Adeepreddy" and password=="Adeepreddy@21":
    print("You sucessfully login")
else:
    print("Sorry Your username or Password is worng")



print("Example of if else statement")  
# Input: Ask the user for their age
age=int(input("Enter your age:"))
#Check whether the age is eligiable to vote or not
eligible=18
if age>eligible:
   print(f"{age} is eligible for vote")
else:
   print(f"{age} is not eligible for vote")   
   

print("Example for if elif else Statement")   
#cheeck whether the give number is positive or negative
number=int(input("Enter any number:")) 
if number>0:
   print(f"{number} is a positive number")
elif number==0:
   print(f"{number} is zero")
else :
   print(f"{number} is negative number")      
   
print("Another example for nested if")   
marks=int(input("Enter your marks:"))

if marks<=100:
   if marks>=90:
      print("You Score A+ grade")
   elif marks>=80:
      print("You Score A grade")   
   elif marks>=70:
      print("You Score B grade")   
   elif marks>=60:
      print("You Score C grade")   
   elif marks>=50:
      print("Yor Score D grade")   
   else:
      print("Sorry Better Luck Next Time You FAILED")   
else:
   print("Please Enter a valid Marks...!!")      
   
   

print("Example for Nested if")
age=int(input("Enter your age to check Whether your age is eligible to enter into club:"))   
has_id=input("Did you have Club id:")

if age>=18:
   if has_id=="yes":
      print("Welcome to CLub...!")
   else:
      print("Sorry you are not eligible to enter in to club")

else:
   print("Sorry your age is not eligible") 


print("Checking Whether Students Marks are Eligible to pass in the exam and passed students are able to enter into clube")
ass=input("Have you complete your assignment:")
if ass=="yes":
    print("Good,What is academics marks")
    
    marks=int(input("Enter Your marks:"))
    if marks<=100:
       
        if marks>=90:
            print("You score A+ Grade,great your eligible to club")
        elif marks>=80:
            print("You score A Grade,great your eligible to club")
        elif marks>=70:
            print("Yorscore B Grade,great your eligible to club")
        elif marks>=60:
            print("You score C Grade,great your eligible to club")
        elif marks>=50:
            print("You score D Grade,great your eligible to club")
        else:
            print("Sorry You scored Fail marks,your Not eligible for Club")
    else:
        print("Please Check What you Entered")        
elif ass=="no":
    print("If you not Complete your assignment your not Eligible for Club Enterence")
else:
    print("Please Provide yes or no")        

         

   
   