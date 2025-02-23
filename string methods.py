#String Methods
a="Adeep Reddy"
print("Original String:",a)
print("\nString Methods:")
print(dir(a))#List of all string methods
print("\nCapitalize Methods:")
print(a.capitalize())
print("\nReplace Method:")
print(a.replace("Reddy","The great"))
print("\nisnumeric Method:")
print(a.isnumeric())
print("\nisalpha Method:")
print(a.isalpha())
print("\nisalnum Methods:")
print(a.isalnum())
print("\nIstitles Method:")
print(a.istitle())
b="    Adeep Reddy   "
print("\n split Method:")
print(b.split())
c="_________Adeep Reddy_________"
print("\n Strip Method:")
print(c.strip('_')) 
print("\n Lstrip Method:")
print(c.lstrip('_'))
print("\n Rstrip Method:")
print(c.rstrip('_'))    
d="HellO WorLd"
print("\n Swapcase Method:")
print(d.swapcase())
print("\n Count Method:")
print(d.count('l'))
print("\n Find Method:")
print(d.find('Wor'))
print("\n capitalize Method:")
print(d.capitalize())
print("\n Case Fold Method:")
print(d.casefold())
print("\n Lower Method:")
print(d.lower())
print("\n Upper Method:")
print(d.upper())
e = "Hello World This is python" 

print("\nSplit Method:") 
print(e.split())

print("\n\nrsplit Method:") 
print(e.rsplit())

# Correcting the rstrip method
print("\nrstrip Method:") 
print(e.rstrip('n'))

# Using split instead of non-existent lsplit
print("\nsplit Method:") 
print(e.split())

# Correcting the lstrip method
print("\nlstrip Method:") 
print(e.lstrip('H'))
