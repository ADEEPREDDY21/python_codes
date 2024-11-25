#There are a set of operators based on different purposes
'''1.Arithmetic operators
   2.Assignment operators
   3.Comparison operators
   4.Logical operators
   5.Identity operators
   6.Membership operators
   7.Bitwise operators'''
#Arithmetic operators
'''Arithmetic operators in Python are used to perform mathematical operations on numbers.
   Addition(+)
   Subtraction(-)
   Multiplication(*)
   Divion(/)
   Floor Division(//)
   Modulus(%)
   rise(**)'''
print("ARITHMETIC OPERATOR")
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
# x=12
# y=34
print(f"addition:{x}+{y}= {x + y}")
print(f"subtraction:{x}-{y}={x-y}")
print(f"Division:{x}/{y}={x/y}")
print(f"Multiplication:{x}*{y}={x*y}")
print(f"Floor:{x}//{y}={x//y}")
print(f"Modulus:{x}%{y}={x%y}")
print(f"rise:{x}**{y}={x**y}")
#In another way we can also write the code
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("Above are Arithmetic operators of {a}and{b}")
print(f"Add:{a+b}")
print(f"Sub:{a-b}")
print(f"Mul:{a*b}")
print(f"Div:{a/b}")
print(f"FloorDiv:{a//b}")
print(f"Mod:{a%b}")
#Assignment operators
'''Assignment operators in Python are used to assign values to variables.
In addition to the basic assignment operator (=), Python supports several
compound assignment operators, which combine arithmetic operations with
assignment.
=
+=
-=
*=
/=
%=
//=
**=
&=
|=
^=
>>=
<<=
'''
print("ASSIGNMENT OPERATOR")
#pyhton is a interpreteded language it can updated old value with new value
#same thing we can do in another way with the help of assignment operators
x=10
print(x)
x+=16
print(x)
e=int(input("Enter e value:"))
e+=10
print(f"e value:{e}")
e-=10
print(f"e value:{e}")
e*=10
print(f"e value:{e}")
e/=10
print(f"e value:{e}")
e%=10
print(f"e value:{e}")
#camparison operators
#A comparison operator, also known as a relational operator, compares values and returns a true or false value
'''< - lessthan to
   > - greaterthan to
   == - equal to
   != - not equal to
   <= - lessthan or equalto
   >= - greaterthan or equal to'''
print("CAMPARISON OPERATOR")
f=int(input("enter f value:"))
print(f"f value is:{f<10}")
print(f"f value is:{f>10}")
print(f"f value is:{f==10}")
print(f"f value is:{f!=10}")
print(f"f value is:{f>=10}")
print(f"f value is:{f<=10}")
# anotherway
print("COMPARISON OPERATOR ANOTHER WAY")
q=int(input("enter q value:"))
w=int(input("enter w value:"))
print(f"q value is:{q<w}")
print(f"q value is:{q>w}")
print(f"q value is:{q==w}")
print(f"q value is:{q!=w}")
print(f"q value is:{q>=w}")
print(f"q value is:{q<=w}")
# logical operator
#A logical operator is a symbol or word that connects two or more expressions to perform a logical calculation.
# and operator is used print boolean value in case of all values are true
# or operator is used to print boolean value in case of any one of the two comparison is true
# not operator is used to print the reverse value pf actual booleaan value 
print("LOGICAL OPERATOR")
k=int(input("Enter k value:"))
l=int(input("Enter l value"))
m=int(input("Enter m value"))
print(k>l and k<m)
print(k==l or k<m)
print(not(k>l))
#identity operator
#The identity operator is an operator that leaves any element it acts on unchanged.
# In programming, it checks if two variables refer to the same object (using is)
print("IDENTITY OPERATOR")
v=["adeep","reddy"]
y=["adeep","reddy"]
z=v
print(v is y)#although v and y variables having same contant
print(v is z)#identity operator will check the whether same memory space or not
print(v is not y)
#membership operators
#A membership operator in Python is used to test whether a value is present in a sequence (like a list, tuple, or string).
print("MEMBERSHIP OPERATOR")
g='adeep'
print('a'in g)# it will check whether a letter is present in g memory space and print it trule
print("s" in g)
