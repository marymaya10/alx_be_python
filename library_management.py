class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        for book in available_books:
            print(book)

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out.")