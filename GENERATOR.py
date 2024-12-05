#Generator function in python
#Generative functions in Python refer to generators,
#which are special functions that yield values one at a time instead of returning them all at once
print("Print Even Numbers using Generator Function")
def my_generator(limit):
    num=0
    while num<limit:
        yield num
        num+=2
        #calling the generator function
n=int(input("Enter the range that should print Even numbers:"))        
even=my_generator(limit=n)
for r in even:
    print(r)        
    
print("Printing Fibonacci series by using Generator function")    
def my_gen(limit):
    x,y=0,1
    while x<limit:
        yield x
        x,y=y,x+y
        #calling the generator function
n=int(input("Enter the range of Fibonacci series:"))        
gen=my_gen(limit=n)
for r in gen:
    print(r)
    
print("Now print odd numbers by using generator funtions")    
def my_odd(limit):
    num=1
    while num<limit:
        yield num
        num+=2
        #calling the generator function
n=int(input("Enter range to print number of odd numbers"))
odd=my_odd(limit=n)
for r in odd:
    print(r)        
        
        