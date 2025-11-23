class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return f"{self.title} is a {self.pages} paged book written by {self.author}"
    
    def __repr__(self):
        #return f"Book('{self.title}, {self.author},{self.pages}')"
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    

book1 = Book("The Power of Habit", "Charles Duhigg", 371)
print(str(book1))     # Calls __str__
print(repr(book1))    # Calls __repr__
    
