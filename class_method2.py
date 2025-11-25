class Person:
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name):
        return cls(name, 0)

person1 = Person("Maggie", 23)
person2 = Person("Ben", 35)
# Creating a child using the class method
child = Person.create_child("Baby Kevin")

print(child.name)  
print(child.age)