from unittest.case import _AssertRaisesContext
from BankAccount import BankAccount
from BankSystem import BankSystem
from Currency import Currency, exchange_to


# Global Test Objects

bank_system = BankSystem()
acct_1 = BankAccount('0001', 'Amy', Currency.USD)
acct_2 = BankAccount('0002', 'Amy', Currency.JPY)
acct_3 = BankAccount('0003', 'Bob', Currency.KRW)
acct_4 = BankAccount('0004', 'Cathy', Currency.USD)
acct_5 = BankAccount('0005', 'David', Currency.USD)
acct_6 = BankAccount('0006', 'Cathy', Currency.USD)
acct_7 = BankAccount('0007', 'Evelyn', Currency.USD)
acct_8 = BankAccount('0008', 'Fred', Currency.EUR)

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
    bank_acct = BankAccount('20230416', 'Amy', Currency.USD)
    assert bank_acct.get_holder_name() == 'Amy'


def test_get_currency():
    bank_acct = BankAccount('20230416', 'Amy', Currency.USD)
    assert bank_acct.get_currency() == Currency.USD


def test_invalid_acct():
    bank_acct = BankAccount('20230416', 'Amy')
    assert bank_acct.is_valid_acct() == False


def test_valid_acct():
    bank_acct = BankAccount('20230416', 'Amy', Currency.USD)
    assert bank_acct.is_valid_acct() == True


def test_deposit():
    acct_1.deposit(25, Currency.USD)
    acct_1.deposit(15, Currency.USD)
    acct_2.deposit(33, Currency.JPY)
    assert acct_1.get_balance() == 40
    assert acct_2.get_balance() == 33


def test_withdraw():
    acct_3.deposit(10, Currency.KRW)
    acct_3.withdraw(5, Currency.KRW)
    assert acct_3.get_balance() == 5


def withdraw_more_than_balance():
    acct_4.deposit(55, Currency.USD)
    acct_4.withdraw(65, Currency.USD)


def test_cannot_withdraw_more_than_balance():
    _AssertRaisesContext(
        Exception,
        withdraw_more_than_balance,
        'The withdraw amount exceeds account balance.',
    )


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
    bank_system.add_acct(BankAccount('20230416', 'Bob', Currency.USD))
    bank_system.add_acct(BankAccount('20230416', 'Catherine', Currency.TWD))


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


def test_transfer():
    acct_5.deposit(100, Currency.USD)
    bank_system.transfer(sender=acct_5, recipient=acct_6, amount=50)
    assert acct_5.get_balance() == 50
    assert acct_6.get_balance() == 50


def test_foreign_transfer():
    acct_7.deposit(10, Currency.USD)
    bank_system.foreign_transfer(acct_7, acct_8, 10)
    assert acct_7.get_balance() == 0
    assert acct_8.get_balance() == 10.891


#  Currency Tests


def test_USD_to_JPY():
    assert exchange_to(Currency.USD, 1, Currency.JPY) == 132.35


def test_TWD_to_USD():
    assert exchange_to(Currency.TWD, 60.96, Currency.USD) == 2
