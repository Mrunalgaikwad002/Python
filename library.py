class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Added: {title} by {author}")

    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books:
                print(f"{book.title} by {book.author}")

                
library = Library()
library.add_book("202", "Python")
library.add_book("Machine Learning", "Jack Dawson")
library.display_books()
