age = 41122
print(id(age))
age = 4033
print(id(age))

class Person:
    def __init__(self, age):
        self.age = age
        
person = Person(age = 42)
print(id(person))
person.age = 56
print(id(person))