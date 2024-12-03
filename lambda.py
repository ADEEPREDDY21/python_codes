#lambda function is a small and anonymous function that can have any number of arguements but only one expression
#Syntax:- lambda arguements:expression
print("Sum of 2 numbers using lambda function")
a=lambda x,y:x+y
x,y=map(int,input("Enter x and y values:").split(" "))
print(a(x,y))

print("Power of numbers")
print("Squares")
square=lambda x:x**2
x=int(input("Enter x value:"))
print(square(x))
print("Cubes")
cube=lambda x:x**3
x=int(input("Enter Required cube value:"))
print(cube(x))
print("Print sqaures for list of values")
n=[2,3,4,5,6,7,8,9]
squared_number=list(map(lambda x:x**2,n))
print(squared_number)

print('Fliter the numbers according to condition')
n=[3,5,7,8,9]
greater_than_3=list(filter(lambda x:x>3,n))
print(greater_than_3)