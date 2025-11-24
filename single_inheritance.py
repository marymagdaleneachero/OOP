class Shape:
    def calculate_area():
        return "Area not defined for generic shape."

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width