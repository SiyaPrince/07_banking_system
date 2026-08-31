from support_operations.validators import account_exists, account_is_active, valid_amount, sufficient_funds
from support_operations.displayers import display_successful_withdrawal

accounts = {}

transactions = []

def create_transaction(account_number, amount):
    transaction = {
        "account": account_number,
        "type": "Withdrawal",
        "amount": amount
    }

    transactions.append(transaction)

def withdraw(account_number, amount):
    accounts[account_number]["balance"] -= amount
    # Select account
    account_number = input("Enter account number: ").strip()

    # Validate account exists
    if not account_exists(accounts, account_number):
        print("Error: Account does not exist.")
        return

    # Validate account is Active
    if not account_is_active(accounts, account_number):
        print("Error: Account is not active.")
        return

    # Get withdrawal amount
    try:
        amount = float(input("Enter withdrawal amount: "))
    except ValueError:
        print("Error: Amount must be a number.")
        return

    # Validate amount > 0
    if not valid_amount(amount):
        print("Error: Withdrawal amount must be greater than 0.")
        return

    # Check sufficient funds
    if not sufficient_funds(account_number, amount):
        print("Error: Insufficient funds.")
        return

    # ONLY NOW mutate state

    # Debit account
    withdraw(account_number, amount)

    # Create transaction record
    create_transaction(account_number, amount)

    # Display success
    display_successful_withdrawal(account_number, amount)