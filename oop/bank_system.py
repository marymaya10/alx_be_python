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
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"Account: {self.account_number}, Holder: {self.holder_name}, Balance: ${self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.02):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"SavingsAccount: {self.account_number}, Holder: {self.holder_name}, Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100}%"


class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=500):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Overdraft limit exceeded")

    def __str__(self):
        return f"CheckingAccount: {self.account_number}, Holder: {self.holder_name}, Balance: ${self.balance}, Overdraft Limit: ${self.overdraft_limit}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def list_accounts(self):
        for account in self.accounts:
            print(account)