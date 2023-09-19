from datetime import date

today = date.today()

class BankAccount:
    
    def __init__(self, acctID, acct_holder, balance):
        self._acct_id = acctID
        self._acct_holder = acct_holder
        self._balance = balance
        self._date_opened = today

    @property
    #getter
    def balance(self):
        return self._balance
        
    #setter
    @balance.setter
    def balance(self, new_balance):
        if self._balance < 0 or self._balance is None:
            print(f'Balance must be greater than 0 -- update salary first')
        self._balance = new_balance

    def make_deposit(self, dep_amt):
        if dep_amt < 0:
            print(f'Deposit amount must be greater than 0')
        else:
            self._balance = self._balance + dep_amt

    def make_withdrawal(self, with_amt):
        if with_amt < 0:
            print(f'Withdrawal amount must be greater than 0')
        else:
            if self._balance - with_amt < 0:
                print(f'Withdrawal amount must be smaller than balance amount')
            else:
                self._balance = self._balance - with_amt

    def transfer(self, amt, target_acct):
        if self._acct_holder is not target_acct._acct_holder:
            print(f'Funds cannot be transferred to accounts with a different account holder')
        else:
            if self._balance - amt < 0:
                print(f'Transfer amount must be less than the origin account balance')
            else:
                self._balance = self._balance - amt
                target_acct._balance = target_acct._balance + amt

    def print_acct_info(self):
        print(f'{self._acct_id = }\t{self._acct_holder = }\t{self._date_opened =}\t{self._balance = }')

