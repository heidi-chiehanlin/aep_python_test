from unittest.case import _AssertRaisesContext
from BankAccount import BankAccount
from BankSystem import BankSystem

# BankAccout Tests


def test_get_acct_no():
    bank_acct = BankAccount('20230416')
    assert bank_acct.get_acct_no() == '20230416'


def test_get_holder_name():
    bank_acct = BankAccount('20230416', 'Amy', 'USD')
    assert bank_acct.get_holder_name() == 'Amy'


def test_get_currency():
    bank_acct = BankAccount('20230416', 'Amy', 'USD')
    assert bank_acct.get_currency() == 'USD'


def test_invalid_acct():
    bank_acct = BankAccount('20230416', 'Amy')
    assert bank_acct.is_valid_acct() == False


def test_valid_acct():
    bank_acct = BankAccount('20230416', 'Amy', 'USD')
    assert bank_acct.is_valid_acct() == True


# BankSystem Tests


def add_invalid_acct_to_system():
    bank_system = BankSystem()
    bank_system.add_acct(BankAccount('20230416'))


def test_add_invalid_acct_to_system():
    _AssertRaisesContext(Exception, add_invalid_acct_to_system)


def add_duplicate_acct_to_system():
    bank_system = BankSystem()
    bank_system.add_acct(BankAccount('20230416', 'Bob', 'USD'))
    bank_system.add_acct(BankAccount('20230416', 'Catherine', 'TWD'))


def test_add_duplicate_acct_to_system():
    _AssertRaisesContext(Exception, add_duplicate_acct_to_system)
