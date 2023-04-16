from unittest.case import _AssertRaisesContext
from BankAccount import BankAccount
from BankSystem import BankSystem

# Global Test Objects

bank_system = BankSystem()
acct_1 = BankAccount('0001', 'Amy', 'USD')
acct_2 = BankAccount('0002', 'Amy', 'JPY')
acct_3 = BankAccount('0003', 'Bob', 'KRW')
acct_4 = BankAccount('0004', 'Cathy', 'USD')
acct_5 = BankAccount('0005', 'David', 'USD')
bank_system.add_acct(acct_1)
bank_system.add_acct(acct_2)
bank_system.add_acct(acct_3)
bank_system.add_acct(acct_4)
bank_system.add_acct(acct_5)


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
    _AssertRaisesContext(
        Exception,
        add_invalid_acct_to_system,
        "The input BankAccount is not valid, provide more information.",
    )


def add_duplicate_acct_to_system():
    bank_system = BankSystem()
    bank_system.add_acct(BankAccount('20230416', 'Bob', 'USD'))
    bank_system.add_acct(BankAccount('20230416', 'Catherine', 'TWD'))


def test_add_duplicate_acct_to_system():
    _AssertRaisesContext(
        Exception,
        add_duplicate_acct_to_system,
        "The input BankAccount already exists and cannot be added again.",
    )


def test_search_acct_function():
    output = bank_system.search_accts_under_clients_name('Amy')
    assert output[0].get_acct_no() == '0001'
    assert output[1].get_acct_no() == '0002'
