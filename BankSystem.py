# Understands the bank accounts in the system
from BankAccount import BankAccount


class BankSystem:
    def __init__(self):
        self._accts = {}

    def add_acct(self, new_acct):
        if new_acct.__class__ != BankAccount:
            raise Exception("Input is not a BankAccount object.")
        if not new_acct.is_valid_acct():
            raise Exception(
                "The input BankAccount is not valid, provide more information."
            )
        self._accts[new_acct.get_acct_no] = new_acct
