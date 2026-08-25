from support_operations.displayers import display_welcome_message, display_menu
    
def run_bank_system():
    customers = []
    accounts = []
    transactions = []

    display_welcome_message()

    while True:
        display_menu()
        operation_choice = input("\nPlease choose operation: ").strip()

        if operation_choice == "1":
            register_customer(customers)
        elif operation_choice == "2":
            view_customers(customers)
        elif operation_choice == "3":
            create_account(accounts)
        elif operation_choice == "4":
            view_accounts(accounts)
        elif operation_choice == "5":
            deposit_money(accounts, transactions)
        elif operation_choice == "6":
            withdraw_money(accounts, transactions)
        elif operation_choice == "7":
            transfer_money(accounts, transactions)
        elif operation_choice == "8":
            view_transaction_history(transactions)
        elif operation_choice == "9":
            view_account_balance(accounts)
        elif operation_choice == "10":
            display_banking_summary(customers, accounts, transactions)
        elif operation_choice == "11":
            print("\nExiting Prince Siya Bank. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
    