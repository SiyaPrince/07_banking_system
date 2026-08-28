def account_exists(account_number):
    return account_number in accounts


def valid_name(name):
    return name.strip() != ""


def valid_balance(balance):
    return balance >= 0