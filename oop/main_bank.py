from bank_system import Account, SavingsAccount, CheckingAccount, Bank

def main():
    # Create a Bank instance
    my_bank = Bank()

    # Create instances of each type of account
    basic_account = Account("123456", "John Doe", 1000)
    savings_account = SavingsAccount("789012", "Jane Smith", 2000, 0.03)
    checking_account = CheckingAccount("345678", "Bob Johnson", 500, 1000)

    # Add accounts to the bank
    my_bank.add_account(basic_account)
    my_bank.add_account(savings_account)
    my_bank.add_account(checking_account)

    # List all accounts in the bank
    my_bank.list_accounts()

if __name__ == "__main__":
    main()