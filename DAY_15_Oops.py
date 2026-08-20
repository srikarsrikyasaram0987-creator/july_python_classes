class ATM:
    def __init__(self,pin,balance=3000,):
        self.pin=pin
        self.balance=balance

    def withdraw(self):
        amount=float(input("Enter the amount: "))
        if amount<=0:
            print("Enter the valid amount: ")
        elif amount>self.balance:
            print("insufficient money in your Account...!")
        else:
            self.balance-=amount
            print("Successfully your amount is withdrawl")

    def check_balance(self):
        print(f"Your current Balance: {self.balance}")

    def deposit(self):
        amount=float(input("Enter the amount: "))
        if amount<=0:
            print("please check valid amount.you printed")
        else:
            self.balance+=amount
            print("Successfully your amount is deposit")

    def change_pin(self):
        old_pin=int(input("Enter your old pin: "))
        if old_pin==self.pin:
            new_pin=int(input("Enter the new pin: "))
            self.pin=new_pin
            print("Pincode has been changed")
        else:
            print("Incorrect pin")
account=ATM(112233)
print("----------WELCOME TO TGB ATM-------------")
Entered_pin=int(input("Enter pin: "))               
if Entered_pin==account.pin:
    while True:
        print("ATM MENU:")
        print("1.Withdraw money")
        print("2.check balance money")
        print("3.Deposit money")
        print("4.Change pin")
        print("5.Exit")
        choice=(input("Enter your choice(1-4): "))
        if choice=="1":
            account.withdraw()
        elif choice=="2":
            account.check_balance()
        elif choice=="3":
            account.deposit()
        elif choice=="4":
            account.change_pin()
        elif choice=="5":
            print("------------THANKS FOR CHOOSING TGB ATM-------------")
            break
        else:
            print("Invalid number")
else:
    print("Invalid pin.Please check...!")                  



1