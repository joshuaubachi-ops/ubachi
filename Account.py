

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
           self.__balance += amount
           print("You have deposited $" + str(amount))
        else:
           print("You have not deposited $" + str(amount))
    def withdraw(self, amount):
        if amount <= 0:
            self.__balance -= amount
            print(f"You have withdrawn ${amount}. Remaining balance is ${self.__balance}")
        else:
            print(f"You have not withdrawn remaining balance is ${self.__balance}")


    def get_balance(self):
        return self.__balance