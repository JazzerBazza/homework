# Bank account classes
class BankAccount:
    no_of_cust = 0
    acc_num = 202300


    def __init__(self, name, mobile_no, initial_depo, pin):
        self.name = name
        self.cust_acc_num = BankAccount.acc_num
        self.mobile_no = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin

        BankAccount.acc_num = BankAccount.acc_num + 1
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1

    def basic_details(self):
        print(f"User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: £{self.acc_balance}")

    def deposit(self):
        amount = int(input("Enter the deposit amount: "))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print(f"Transaction completed. Current balance: £{self.acc_balance}")
        else:
            print("Invalid amount. Transaction aborted")

    def withdraw(self):
        amount = int(input("Enter the withdrawal amount: "))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            print(f"Transaction completed. Current Balance: £{self.acc_balance}")
        else:
            print("Invalid amount. Transaction aborted")

    def payment(self, other):
        amount = int(input("Enter the payment amount: "))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            print(f"Transaction completed. Current balance: {self.acc_balance}")
        else:
            print("Invalid amount. Transaction aborted")



