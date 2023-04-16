# Understands the information of a unique bank account
class BankAccount:
    def __init__(self, acct_no, name='unknown', currency='unknown'):
        self._acct_no = acct_no
        self._holder_name = name
        self._currency = currency

    def get_acct_no(self):
        return self._acct_no

    def get_holder_name(self):
        return self._holder_name

    def get_currency(self):
        return self._currency

    def is_valid_acct(self):
        return self._holder_name != 'unknown' and self._currency != 'unknown'
