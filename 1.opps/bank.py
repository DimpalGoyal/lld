class Bank:
    def __init__(self, name:str, balance:int ) -> None:
        self.__balance:int = balance
        self.name:str = name
        print("\n*****")
        print(f"name: {name}")
        print(f"balance: {balance}")
        print("***** \n")
    
    def deposit(self, amount:int) -> None:
        self.__balance += amount
        print(f"\namount {amount} is deposited")

    def withdraw(self, amount:int) -> None:
        if amount > self.__balance:
            print("not enough money")
        else:
            self.__balance -= amount
            print(f"amount {amount} is withdrawed\n")
            print(f"total balance is: {self.__balance}")

acc = Bank("dimpal", 1000)
acc.deposit(1000)
acc.withdraw(200)