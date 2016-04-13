## Everything is an object

Anytime that you have some variable name pointing being assigned to a value think of an arrow pointing to an object that has an id, type, and value.

## Mutable vs Immutable
Essentially values that can change are mutable and those that cannot are immutable. For example the data type int is immutable, if you assign an int to another value 
then the id will change for that int. In Python the variable will be assigned to another integer object with that value.

```python
age = 41122
print(id(age))
age = 4033
print(id(age))
```

Where as if we has a person object and change the int value on it, the person object would not change it's id. Only the int.
i.e.

```python
#Person is a predefined class
person = Person(age = 42)
print(id(person))
person.age = 56
print(id(person))
```

##Numbers

With python integers there is an unlimited range.
i.e. 
```python
2 ** 1024 # Large number
```

There is also a difference in divion, / - will get a floating point number and // - represents integer division that is the same as 
Java and C#. ** Remeber ** python rounds toward negative infinity, therefore if you preform integer division on 7//4 it will reselt in 2.
Though truncation is done toward 0.

```python
    7/4 # 1.75
    7//4 # 1
```

There are also the data type bool (True or False), real (3.14), decimal(3.14). Bool is a subtype of integer therefore it can be 
treated just like a number, or simply treat it like a boolean. Real is comparable to a floating point number, it has serious floating point errors 
even on smaller numbers. Then there is the decimal type that handles the floating point issues quite nicely. In addition there is support for fractions.

```python
    myBool = True
    myBool = (1) # True
    myBool = (0) # False
    
    myReal = 3.14
    
    from decimal import Decimal
    myDecimal = Decimal(3.14) 
```

The next type is a string.

