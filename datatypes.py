'''Python has several data types that help identify the type of data being used, its size, and the functions associated with it
 Numeric: Stores numeric values, such as integers, floats, and complex numbers: 
   Integer: Stores whole numbers, such as 1, -99, 10, 25, etc. 
   Float: Stores decimal numbers, such as 3.14, -0.001, 2.5e2, etc. 
   Complex: Stores complex numbers, such as 2+4i, 6-8i, etc. 
 Sequence: Organizes and stores multiple values efficiently, such as lists and tuples: 
   List: Groups related data, represented using square brackets 
   Tuple: Ordered collections of objects, represented using round brackets 
 String: Represents text data, such as "ABCD" 
 Boolean: Represents truth values, such as True or False 
 NoneType: Represents the absence of value, similar to Python's Null from other programming languages 
Python is a dynamically typed language, so you don't need to explicitly declare the type of a variable. Data types are set when you assign a value to a variable. 
'''
#int
print(10)
print(type(234))
#float
print(23.45)
print(type(234.3))
print(23e3)
print(type(23e3))
#complex
print(23+3j)
print(type(23e3j))

#boolean
print(True)
print(False)
print(type(True))
print(type(False))
#None data type
print(None)
print(type(None))
#sequence
#strings
print("ADEEPREDDY")
print('ADEEPREDDY')
print(type('ADEEPREDDY'))
#list
l1=[1,3,"adeep",3.4]
print(l1)
print(type(l1))
print(l1[2:4])
#tuple
t1=(23,545,"adeep",93.5)
print(t1)
print(type(t1))
print(t1[1:4])
#set which are mutable but unorder
s1={10,34,32,23,"adeep"}
print(s1)
print(type(s1))
#Dictionary datatype
d1={"Name":"ADEEP","age":21,"Place":"Tadepalligudem","Number":9441182329}
print(d1)
print(type(d1))