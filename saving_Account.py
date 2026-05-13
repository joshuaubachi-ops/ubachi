from Account import Account

class SavingAccount(Account):
    def __init__(self, owner, balance=0 ,interest_rate=0.02, withdrawal_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit
        self.balance = balance
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f'Interest: {interest} Applied')
    def withdraw(self, amount):
        if amount <= self.balance:
            self.deposit(amount)
            print(f'Withdrawn: {amount}')
        else:
            print(f'Withdrawn: {amount}')






print("---Saving Account---")
savings = SavingAccount("savings", balance=1000, interest_rate=0.02)
savings.apply_interest()
savings.withdraw(100)