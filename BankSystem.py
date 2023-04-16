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
        if new_acct.get_acct_no in self._accts.keys():
            raise Exception(
                "The input BankAccount already exists and cannot be added again."
            )
        self._accts[new_acct.get_acct_no] = new_acct

    def search_accts_under_clients_name(self, name):
        output = []
        for acct in self._accts.keys():
            if self._accts[acct].get_holder_name() == name:
                output.append(self._accts[acct])
        sorted_output = sorted(output, key=lambda x: x.get_acct_no())
        return sorted_output
