accounts = {}

transactions = []


def account_exists(account_number):
    return account_number in accounts


def account_is_active(account_number):
    return accounts[account_number]["status"] == "Active"


def valid_amount(amount):
    return amount > 0


def sufficient_funds(account_number, amount):
    return accounts[account_number]["balance"] >= amount


def withdraw(account_number, amount):
    accounts[account_number]["balance"] -= amount


def create_transaction(account_number, amount):
    transaction = {
        "account": account_number,
        "type": "Withdrawal",
        "amount": amount
    }

    transactions.append(transaction)


def display_success(account_number, amount):
    print("\nWithdrawal successful!")
    print(f"Account Number: {account_number}")
    print(f"Amount Withdrawn: R{amount:.2f}")
    print(f"New Balance: R{accounts[account_number]['balance']:.2f}")


def main():
    # Select account
    account_number = input("Enter account number: ").strip()

    # Validate account exists
    if not account_exists(account_number):
        print("Error: Account does not exist.")
        return

    # Validate account is Active
    if not account_is_active(account_number):
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
    display_success(account_number, amount)


main()