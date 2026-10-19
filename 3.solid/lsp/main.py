from savings_account import SavingsAccount
from fixed_deposit import FixedDepositAccount

s = SavingsAccount(1000)
s.deposit(1000)
s.withdraw(400)

fd  = FixedDepositAccount(1000)
fd.deposit(2000)