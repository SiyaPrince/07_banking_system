from support_operations.validators import account_exists, valid_balance, valid_name
from support_operations.displayers import display_account

accounts = {}

def create_account(account_number, name, balance):
    accounts[account_number] = {
        "name": name,
        "status": "Active",
        "balance": balance
    }

    # Get account number
    account_number = input("Enter new account number: ").strip()

    # Validate account number
    if account_number == "":
        print("Error: Account number cannot be empty.")
        return

    if account_exists(account_number):
        print("Error: Account already exists.")
        return

    # Get account holder name
    name = input("Enter account holder name: ").strip()

    if not valid_name(name):
        print("Error: Name cannot be empty.")
        return

    # Get opening balance
    try:
        balance = float(input("Enter opening balance: "))
    except ValueError:
        print("Error: Balance must be a number.")
        return

    if not valid_balance(balance):
        print("Error: Balance cannot be negative.")
        return

    # ONLY NOW mutate state
    create_account(account_number, name, balance)

    # Display success
    display_account(accounts, account_number)