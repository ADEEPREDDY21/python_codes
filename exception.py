#Exception are raised the program as syntactically correct, but the code result is an error
#However it can changes the normal flow of the program
print("\n1:")
try:
    print(X)#it is name error that means the name or variable that didn't declare in the following code
except:
    print("An Exception occured")   
    
print("\n2:")     
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something went wrong..!")#this statement will print whether there is no exception error  
    
print("\n3:")          
try:
    print(x=10)
except NameError:
    print("Variable not declared") #in this case this statement will skips due the variable x is assigned to a value   
except:
    print("Something went wrong..!") #so that there is no exception error and print this statement
    
print("\n4:")  
try:
    print(x)
except NameError:
    print("Something went wrong")    
else:
    print("Nothing went wrong")   
    
print("\n5:")     
x=5
try:
    print(x)
except NameError:
    print("something went wrong")    
else:
    print("Nothing went wrong")    
    
print('\n6:')    
try:
    print(z)
except:
    print('Something went wrong')    
finally:
    print('Nothing went wrong..!')  
    
print("\n7:")      
a=12
b="adeep"
try:
    print(z=a+b)
except TypeError:
    print("Something went wrong")    
else:
    print("nothing went wrong")
    