from withdrawable_account import WithdrawableAccount

class SavingsAccount(WithdrawableAccount):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self,amount):
        self.balance += amount 
        print(f'amount despoited, total balance = {self.balance}')
    

    def withdraw(self, amount):
        if self.balance < amount:
            print("cannot withdraw, insufficent balance")
        else:
            self.balance -= amount
            print(f"amount {amount} withdrawn, remaining balance: {self.balance}")