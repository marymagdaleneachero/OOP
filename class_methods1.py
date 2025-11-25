class Book:
    total_books = 0
    
    def __init__(self):
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        return f"Total number of books created is {cls.total_books}"
    
book1 = Book()
book2 = Book()
Book.display_total_books()