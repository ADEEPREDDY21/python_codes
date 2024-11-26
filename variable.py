'''A variable in Python is a named container that stores data values in a computer's memory'''
#python is a dynamic programming language that means no need to mention any datatypes 
#it will take datatype by given value
#examples
a=23
print(a)
a=b=c=420
print(c)
print(b)
print(a)
adeep=212
print(adeep)
print("adeep")#if we use "" then it will consider as string value
re="adeep"
print(re)
#there are set of variable rules in python prgramming language
#1.Must start with a letter or an underscore
#2.Cannot start with a number
#3.Can only contain Letters,numbers and underscores
#4.Variables Names are case sensitive
#5.Python key words or reserved words are cannot be used in as variable names
age=12
Age=23
AGE=34
#coming to these case the 3 elements are consider as 3 different variables
print(age)
print(Age)
print(AGE)
#we can also assign values in terminal space by using input
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
z=x+y
print("z value:",z)
#Assigning Multiple Values
j=k=l=23
print(j,k,l,sep="\n")
print(j,k,l,sep="\t")
print(j,k,l,sep="***")#sep key word is used for seperate function
                      #By using sep="" we can creat seperate space
#Multiple value to Multiple Variable
f,g,h="adeep","reddy","velagala"
print(f,g,h)
#Variable Name Which Has Meaning/Purpose
Maths=34
Python=65
Total=Maths+Python
print(Total)#By Assigning a vlue to meaningful word so that other deveplor and easily understand 
#Multable Words in Same Variable Name
#So that we can use word for different values in complex code
totalpay=34#camelcase
Totalpay=45#pascalcase
total_pay=35#snakecase
#Constant value generally use CAP letters
PI=3.14
GRAVITY=9.8