class BankAccount:
    def __init__(self, acct_no: str) -> None:
        self._acct_no = acct_no

    def get_acct_no(self) -> str:
        return self._acct_no
