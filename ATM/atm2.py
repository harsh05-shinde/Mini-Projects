#Uisng class

class atm:
    def __init__(self,total_amount):
        self.total_amount = total_amount
        print(f"the total amount is {total_amount}")

    def deposite(self,deposite_amount):
        self.total_amount = self.total_amount + deposite_amount
        print(f"The total amount is after depositing {self.total_amount}")
    def withdraw(self,withdraw_amount):
        self.total_amount = self.total_amount - withdraw_amount
        print(f"the amount after withdraw is {self.total_amount}")

d1 = int(input("Enter Your initial amount:"))
atm_machine = atm(d1)
atm_machine.deposite(12)
atm_machine.withdraw(20)
#d1.check_balance(2000)
#d1.deposite(100)