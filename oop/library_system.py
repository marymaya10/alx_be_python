# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library
class Library:
    def __init__(self):
        self.books = []  # list to store any Book type

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
# Base Class - Account
class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account {self.account_number}: {self.holder_name}, Balance: ${self.balance}"


# Derived Class - SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.02):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"SavingsAccount {self.account_number}: {self.holder_name}, Balance: ${self.balance}, Interest Rate: {self.interest_rate*100}%"


# Derived Class - CheckingAccount
class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=100):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"CheckingAccount {self.account_number}: {self.holder_name}, Balance: ${self.balance}, Overdraft Limit: ${self.overdraft_limit}"


# Composition - Bank
class Bank:
    def __init__(self):
        self.accounts = []  # list to store any Account type

    def add_account(self, account):
        self.accounts.append(account)

    def list_accounts(self):
        for account in self.accounts:
            print(account)


# Example usage for Bank
if __name__ == "__main__":
    # Library example (already above)

    # Bank example
    bank = Bank()

    # Add accounts
    savings = SavingsAccount("SA001", "Alice", 1000, 0.03)
    checking = CheckingAccount("CA001", "Bob", 500, 200)

    bank.add_account(savings)
    bank.add_account(checking)

    # Perform operations
    savings.deposit(200)
    checking.withdraw(100)

    # List all accounts
    bank.list_accounts()

# Example usage
if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("1984", "George Orwell")
    ebook1 = EBook("Digital Fortress", "Dan Brown", 1200)
    printbook1 = PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 180)

    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)

    # List all books
    library.list_books()
