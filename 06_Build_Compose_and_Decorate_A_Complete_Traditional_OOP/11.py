# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

# Create a class book
class Book:
    # class variable
    total_books = 0

    # constructor for initialization
    def __init__(self, book_name):
        self.book_name = book_name
        # increment the total books
        Book.total_books += 1

    # used class method for increment the books
    @classmethod
    def increment_book_count(cls):
        return cls.total_books 
    

# storing data
book1 = Book("The Psychology of Money")
book2 = Book("Atomic Habits")
book3 = Book("Thinking, Fast and Slow")
book4 = Book("Rich Dad Poor Dad")
book5 = Book("Mindset")

# Printing data
print(f"{book1.book_name}\n{book2.book_name}\n{book3.book_name}\n{book4.book_name}\n{book5.book_name}\nTotal number of books: {book1.increment_book_count()}")

# Output: 
# The Psychology of Money
# Atomic Habits
# Thinking, Fast and Slow
# Rich Dad Poor Dad
# Mindset
# Total number of books: 5