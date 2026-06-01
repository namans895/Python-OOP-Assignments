# Library Management System

class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added to library")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(title, "issued successfully")
                return
        print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(book.title, "returned successfully")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print("-", book.title)


# Creating library
lib = Library()

b1 = Book("Python Basics")
b2 = Book("Data Structures")
b3 = Book("Machine Learning")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.display_books()

lib.issue_book("Data Structures")

lib.display_books()

lib.return_book(b2)

lib.display_books()
