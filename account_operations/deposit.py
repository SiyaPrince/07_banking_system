from support_operations.displayers import display_successful_deposit
from support_operations.validators import valid_amount, account_exists, account_is_active

accounts = {}

transactions = []

def create_transaction(account_number, amount):
    transaction = {
        "account": account_number,
        "type": "Deposit",
        "amount": amount
    }

    transactions.append(transaction)

def deposit(account_number, amount):
    accounts[account_number]["balance"] += amount

    # Select account
    account_number = input("Enter account number: ").strip()

    # Validate account exists
    if not account_exists(accounts, account_number):
        print("Error: Account does not exist.")
        return

    # Validate account is Active
    if not account_is_active(account_number):
        print("Error: Account is not active.")
        return

    # Get deposit amount
    try:
        amount = float(input("Enter deposit amount: "))
    except ValueError:
        print("Error: Amount must be a number.")
        return

    # Validate amount > 0
    if not valid_amount(amount):
        print("Error: Deposit amount must be greater than 0.")
        return

    # ONLY NOW mutate state

    # Credit account
    deposit(account_number, amount)

    # Create transaction record
    create_transaction(account_number, amount)

    # Display success
    display_successful_deposit(accounts, account_number, amount)