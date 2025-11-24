class Dog:
    def make_sound(self):
        print("WOOF")
class Cat:
    def make_sound(self):
        print("MEOW")

class Bird:
    def make_sound(self):
        print("WHOOSH")

def let_them_speak(animals):
    for animal in animals:
        animal.make_sound()

animals = [Dog(), Cat(), Bird()]
let_them_speak(animals)


