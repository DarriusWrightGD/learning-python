myBool = True
print(myBool)
myBool = bool(1) # True
print(myBool)
myBool = bool(0) # False    
print(myBool)
    
myReal = 3.14
print(myReal)
    
from decimal import Decimal
myDecimal = Decimal('3.14') 
print(myDecimal)

myString1 = 'This is a string'
myString2 = "This is a string"
myString3 = '''This is a 
multi line string.'''
myString4 = """Also multi line
string."""

print(myString1)
print(myString2)
print(myString3)
print(myString4)

print(len(myString1))
print(myString1.encode('utf-8'))
print(myString1.encode('utf-8').decode('utf-8'))