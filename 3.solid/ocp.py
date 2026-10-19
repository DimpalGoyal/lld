from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount:int):
        pass


class UPIPayment(Payment):
    def pay(self, amount:int):
        print(f"paying through upi of Rs.{amount}")

class BankPayment(Payment):
    def pay(self, amount:int):
        print(f"paying through bank of Rs.{amount}")

class CardPayment(Payment):
    def pay(self, amount:int):
        print(f"paying through card of Rs.{amount}")


###---####
class paymentProcessor:
    def process_payment(self, payment_method: Payment, amount:int):
        payment_method.pay(amount)

upi = UPIPayment()
pay_process = paymentProcessor()

pay_process.process_payment(upi, 400)