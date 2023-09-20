import io
import sys
from unittest import TestCase, main
from BankAccount import BankAccount

class TestBankAccountClass(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.acct_4_test = BankAccount(100, "Joe Smith", 1_000)
        cls.diff_acct = BankAccount(100, "Jane Doe", 1_000)

    def test_setting_balance_negative_raises_exception(self):
        with self.assertRaises(ValueError):
            self.acct_4_test.balance = -1000

    def test_2_deposit_increases_balance_by_200(self):
        existing = self.acct_4_test.balance
        self.acct_4_test.make_deposit(200)
        new = self.acct_4_test.balance
        self.assertEqual(existing + 200, new, f"Expected {existing + 200}, got {new}")
    # Can't run this in PyCharm!!!!!'
    # Run from terminal
    def test_negative_deposit_amt_writes_error(self):
        bad_dep_amt = -200
        expected_diag = f'Value {bad_dep_amt} invalid for deposit amount; no change made\n'
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        self.acct_4_test.make_deposit(bad_dep_amt)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), expected_diag)

    def test_different_bank_accts_cannot_xfer_funds(self):
        with self.assertRaises(ValueError):
            self.acct_4_test.transfer(300, self.diff_acct)

    # Not really necessary.....
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.acct_4_test
        del cls.diff_acct

if __name__ == "__main__":
    main()