accounts = {
    "1001": {
        "name": "Alice",
        "status": "Active",
        "balance": 5000.00
    },
    "1002": {
        "name": "Bob",
        "status": "Inactive",
        "balance": 2500.00
    }
}

transactions = []


def account_exists(account_number):
    return account_number in accounts


def account_is_active(account_number):
    return accounts[account_number]["status"] == "Active"


def valid_amount(amount):
    return amount > 0


def deposit(account_number, amount):
    accounts[account_number]["balance"] += amount


def create_transaction(account_number, amount):
    transaction = {
        "account": account_number,
        "type": "Deposit",
        "amount": amount
    }

    transactions.append(transaction)


def display_success(account_number, amount):
    print("\nDeposit successful!")
    print(f"Account Number: {account_number}")
    print(f"Amount Deposited: R{amount:.2f}")
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
    display_success(account_number, amount)


main()