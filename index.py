# Define a simple Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"This book is '{self.title}' by {self.author}.")

# Create a Book object
my_book = Book("Neon Dreams", "Samuel M")

# Use the method
my_book.describe()
