accounts = {}


def account_exists(account_number):
    return account_number in accounts


def display_account(account_number):
    account = accounts[account_number]

    print("\n--- Account Details ---")
    print(f"Account Number: {account_number}")
    print(f"Account Holder: {account['name']}")
    print(f"Status: {account['status']}")
    print(f"Balance: R{account['balance']:.2f}")


def view_account():
    # Select account
    account_number = input("Enter account number: ").strip()

    # Validate account exists
    if not account_exists(account_number):
        print("Error: Account does not exist.")
        return

    # Display account details
    display_account(account_number)


def main():
    view_account()


main()