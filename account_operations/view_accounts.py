from support_operations.validators import account_exists
from support_operations.displayers import display_account

accounts = {}

def view_account():
    # Select account
    account_number = input("Enter account number: ").strip()

    # Validate account exists
    if not account_exists(accounts, account_number):
        print("Error: Account does not exist.")
        return

    # Display account details
    display_account(accounts, account_number)