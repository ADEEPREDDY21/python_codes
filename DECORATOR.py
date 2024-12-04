#decorator funtion is a function that wrapper the another function
#which allows to modify the existing function without permanently changing it
print('Example for decorative funtion')
def my_decorator(function):
    def wrapper():
        print('Something is happening Before a function is called')
        function()
        print('Something is happening After a function is called')
    return wrapper
#now we can use the decorator function to decorate the existing function
@my_decorator#Here @ decorator name is mentions to call a function
def say_hello():
    print("Hello,World..!")
say_hello()    


print("repeat a value with decorator")
def repeat(number):
    def decorator(function):
        def wrapper():
            for r in range(number):
                print(f"Repeating the number {r} time")
                function()
        return wrapper
    
    return decorator
#now we can use the decorator function to decorate the existing function
n=int(input("Enter how many time you want to repeat the value:"))
@repeat(n-1)
def greeting():
    print("Hello,World..!")
greeting()    


print("Repeat the different names with decorator")
def repeat(number):
    def decorator(function):
        def wrapper(*args,**kwargs):
            for r in range(number):
                print(f"Repeating the value {r+1} time")
                function(*args,**kwargs)
        return wrapper
    return decorator
#now we can use the decorator function to decorate the existing function
n=int(input("Enter number of time should a value repeat"))
@repeat(n)

def greeting(names):
    for i in names:
        print(f"Hello,{i}..!")
    
names=["Adeep","Reddy","Haritha","Suresh"]    
greeting(names)