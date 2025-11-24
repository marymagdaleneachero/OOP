class Bird:
    def fly(self):
        print("This bird is flying")
class Mammal:
    def run(self):
        print("This mammal is running")

class Bat(Bird, Mammal):
    pass

bat = Bat()
bat.fly()
bat.run()