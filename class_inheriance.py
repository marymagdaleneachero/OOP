class Animal:
    def eat():
        print("The animal is eating.")


    def sleep():
        print("The animal is sleeping.")

class Dog(Animal):
    def bark():
        print("The dog is barking.")

animal1 = Animal()
animal1.eat()
animal1.sleep()

dog1 = Dog()
dog1.eat()     
dog1.sleep()   
dog1.bark()