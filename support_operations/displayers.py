def display_welcome_message():
    print("=" * 45)
    print("\nWelcome to Prince Siya Bank")
    print("=" * 45)

def display_menu():
    print("=" * 45)
    print()
    print("1. Register Customer")
    print("2. View Customers")
    print("3. Create Account")
    print("4. View Accounts")
    print("5. Deposit Money")
    print("6. Withdraw Money")
    print("7. Transfer Money")
    print("8. View Transacion History")
    print("9. View Account Balance")
    print("10. Display Banking Summary")
    print("11. Exit")
    print("=" * 45)

def display_account(accounts, account_number):
    account = accounts[account_number]

    print("\nAccount created successfully!")
    print(f"Account Number: {account_number}")
    print(f"Account Holder: {account['name']}")
    print(f"Status: {account['status']}")
    print(f"Balance: R{account['balance']:.2f}")

