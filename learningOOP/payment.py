"""
 the payslip function  represent payment information for individuals.
The class has three attributes: name (representing the person's name),
payment (a string indicating whether the person has been paid or not, initially set to "no"),
and amount (representing the payment amount).
"""
class payslip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def payment_status(self):
        if self.payment == "yes":
            return "Mr " + (self.name) + " has been paid $" + str((self.amount))
        else:
            return "Mr " + (self.name) + " is yet to be paid"


muslim = payslip("muslim", "no", 3000)
bello = payslip("bello", "no", 3000)
print(muslim.payment_status())
print(bello.payment_status())

muslim.pay()
print("After payment")
print(muslim.payment_status())
print(bello.payment_status())
