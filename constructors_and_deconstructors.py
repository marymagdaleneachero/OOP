class Person:
    def __init__(self, name, age):
        self.name = name
        self.age - age

    def __del__(self):
        # Destructor: runs when the object is about to be deleted
        print(f"Goodbye {self.name}! The Person object is being deleted.")
