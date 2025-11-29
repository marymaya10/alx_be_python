from library_management import Library, Book

def main():
    # Create a library
    library = Library()

    # Add books
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)

    print("Available books after setup:")
    library.list_available_books()

    # Checkout a book
    library.checkout_book("1984")

    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Return the book
    library.return_book("1984")

    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
