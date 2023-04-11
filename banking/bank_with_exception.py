# This is my banking script with an exception generated in case of an error in the script.
# The program is still under development.

from bank import BankAccount
try:
    cust1 = BankAccount(name="Barrie", mobile_no=7220345678, initial_depo=250, pin=1234)
    cust2 = BankAccount(name="Esme", mobile_no=7768491260, initial_depo=250, pin=4321)
    cust3 = BankAccount(name="Tom", mobile_no=7868491390, initial_depo=400, pin=4132)

    pprint("No, of customers is", BankAccount.no_of_cust)
    print(cust1.basic_details())
    print(cust2.basic_details())
    print(cust3.basic_details())
    cust1.deposit()
    print(cust1.basic_details())
    cust1.withdraw()
    print(cust2.basic_details())
    cust2.payment(cust3)
    print(cust3.basic_details())

except:
    print("There is currently a system error. Please try again later.")

