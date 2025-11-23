class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return f"{self.title} is a {self.pages} paged book written by {self.author}"
    
    def __repr__(self):
        return f"Item('{self.title}, {self.author},{self.pages}')"
    
