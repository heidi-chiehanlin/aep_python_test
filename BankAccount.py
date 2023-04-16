# Understands the information of a unique bank account
class BankAccount:
    def __init__(self, acct_no, name='unknown', currency='unknown'):
        self._acct_no = acct_no
        self._holder_name = name
        self._currency = currency
        self._balance = 0

    def get_acct_no(self):
        return self._acct_no

    def get_holder_name(self):
        return self._holder_name

    def get_currency(self):
        return self._currency

    def is_valid_acct(self):
        return self._holder_name != 'unknown' and self._currency != 'unknown'

    def deposit(self, amount, currency):
        if currency != self._currency:
            raise Exception("The currency is not matched.")
        else:
            self._balance += amount

    def withdraw(self, amount, currency):
        if currency != self._currency:
            return Exception("The currency is not matched.")
        if amount > self._balance:
            raise Exception("The withdraw amount exceeds account balance.")
        self._balance -= amount

    def get_balance(self):
        return self._balance
