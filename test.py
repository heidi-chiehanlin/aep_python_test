from BankAccount import BankAccount


def test_get_acct_no():
    bank_acct = BankAccount('20230416')
    assert bank_acct.get_acct_no() == '20230416'


def test_get_holder_name():
    bank_acct = BankAccount('20230416', 'Amy', 'USD')
    assert bank_acct.get_holder_name() == 'Amy'


def test_get_currency():
    bank_acct = BankAccount('20230416', 'Amy', 'USD')
    assert bank_acct.get_currency() == 'USD'


def test_unvalid_acct():
    bank_acct = BankAccount('20230416', 'Amy')
    assert bank_acct.is_valid_acct() == False


def test_valid_acct():
    bank_acct = BankAccount('20230416', 'Amy', 'USD')
    assert bank_acct.is_valid_acct() == True
