def account_exists(accounts, account_number):
    return account_number in accounts

def account_is_active(accounts, account_number):
    return accounts[account_number]["status"] == "Active"

def valid_amount(amount):
    return amount > 0

def valid_name(name):
    return name.strip() != ""

def valid_balance(balance):
    return balance >= 0