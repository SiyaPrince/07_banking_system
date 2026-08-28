from datetime import datetime

# Example account data
accounts = {}

# Store transaction records
transactions = []


# Select sender account
sender_account = input("Enter sender account number: ").strip()

# Validate sender exists and is Active
if sender_account not in accounts:
    print("Error: Sender account does not exist.")

elif accounts[sender_account]["status"] != "Active":
    print("Error: Sender account is not active.")

else:
    # Select receiver account
    receiver_account = input("Enter receiver account number: ").strip()

    # Validate receiver exists and is Active
    if receiver_account not in accounts:
        print("Error: Receiver account does not exist.")

    elif accounts[receiver_account]["status"] != "Active":
        print("Error: Receiver account is not active.")

    # Ensure sender != receiver
    elif sender_account == receiver_account:
        print("Error: Sender and receiver cannot be the same account.")

    else:
        # Get amount
        try:
            amount = float(input("Enter transfer amount: "))

            # Validate amount > 0
            if amount <= 0:
                print("Error: Transfer amount must be greater than 0.")

            # Check sender has sufficient funds
            elif accounts[sender_account]["balance"] < amount:
                print("Error: Sender has insufficient funds.")

            else:
                # ONLY NOW mutate state

                # Debit sender
                accounts[sender_account]["balance"] -= amount

                # Credit receiver
                accounts[receiver_account]["balance"] += amount

                # Create transaction record
                transaction = {
                    "sender": sender_account,
                    "receiver": receiver_account,
                    "amount": amount,
                    "date": datetime.now(),
                    "type": "Transfer"
                }

                transactions.append(transaction)

                # Display success
                print("\nTransfer successful!")
                print(f"From: {accounts[sender_account]['name']} ({sender_account})")
                print(f"To: {accounts[receiver_account]['name']} ({receiver_account})")
                print(f"Amount: R{amount:.2f}")
                print(
                    f"Sender balance: "
                    f"R{accounts[sender_account]['balance']:.2f}"
                )
                print(
                    f"Receiver balance: "
                    f"R{accounts[receiver_account]['balance']:.2f}"
                )

        except ValueError:
            print("Error: Please enter a valid numeric amount.")