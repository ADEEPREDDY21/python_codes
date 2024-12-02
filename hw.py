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

#print("To print gcd of 2 number")
def gcd(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return abs(num1)
num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))
GCD=gcd(num1,num2)
print(GCD)

         
         
