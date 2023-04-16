from BankAccount import BankAccount


def test_get_acct_no():
    bank_acct = BankAccount('20230416')
    assert bank_acct.get_acct_no() == '20230416'
