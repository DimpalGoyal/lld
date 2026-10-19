from abc import abstractmethod
from account import Account

class WithdrawableAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    @abstractmethod
    def withdraw(self, amount):
        pass