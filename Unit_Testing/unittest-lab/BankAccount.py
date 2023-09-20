from datetime import datetime


class BankAccount:
    def __init__(self, acct_ID, acct_holder, init_balance):
        self._acct_ID = acct_ID
        self._acct_holder = acct_holder
        self._date_opened = datetime.now()
        self.balance = init_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_bal):
        """
        Test if invalid balance for setter (-1000) throws exception
        'Value -1000 invalid for balance field; no change made'
        """
        if 0 < new_bal:
            self._balance = new_bal
        else:
            raise ValueError(f'Value {new_bal} invalid for balance field; no change made')

    # Make a deposit - keep it simple
    def make_deposit(self, dep_amt):
        """
        Test if invalid balance for make_deposit prints diagnostic


        Test if adding 200 to existing balance increases existing balance by 200
        """
        if 0 < dep_amt:
            self.balance += dep_amt
        else:
            print(f'Value {dep_amt} invalid for deposit amount; no change made')

    # Make a withdrawal - no overdrafts allowed
    def make_withdrawal(self, with_amt):
        if 0 < with_amt:
            self.balance -= with_amt
        else:
            print(f'Value {with_amt} invalid for withdrawal amount; no change made')

    # Transfer(not the best way to do this)
    # Account owners must be the same
    def transfer(self, trans_amt, other_acct):
        '''
        Test if same account holder raises exception
        '''
        if self._acct_holder == other_acct._acct_holder:
            if self.balance - trans_amt < 0:
                diag = (f"Insufficient funds in account with ID {self._acct_ID}"
                       f"Required: {trans_amt}: Available: {self.balance}. Transfer not completed")
                raise ValueError(diag)
            else:
                self.make_withdrawal(trans_amt)
                other_acct.make_deposit(trans_amt)
        else:
            raise ValueError('Account holders not the same; no changes made')

    # Print account particulars
    def print_acct_info(self):
        print(f'{"*" * 50}\nAccount info for account ID: {self._acct_ID}')
        print(f'Holder: {self._acct_holder}\tDate opened: {self._date_opened}\tBalance: {self.balance:,}\n{"*" * 50}')

if __name__ == '__main__':

    import doctest
    doctest.testmod()
