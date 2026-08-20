from datetime import datetime
class ATM:
    def __init__(self,name,account_no,balance):
        self.name=name
        self.account_no=account_no
        self.__balance=balance
        self.transcations=[]
    def check_balance(self):
        print(f"your balance: {self.__balance}")
    def deposit(self,amount):
        self.balance=self.__balance+amount
        self.transcations.append("Deposit:"+str(amount))
        print("Money deposited: ",amount)
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            self.transcations.append("withdraw:"+str(amount))
            print("Money withdrawal: ",amount)
        else:
            print("Insufficient Balance!....In your account")

    def show_balance(self):
            print(f"your balance: {self.__balance}")
    def mini_statement(self):
            print("\n------Mini Statement-----") 
            for transcation in self.transcations:
                print(transcation)
                print("Current balance: ",self.__balance)
class saving_acc(ATM):
     def withdraw(self,amount):
          print("Saving Account")
          super().withdraw(amount)
class current_acc(ATM):
     def withdraw(self,amount):
          print("Current Account")
          super().withdraw(amount)
customer=saving_acc("srikar","12345",2000)
print("-"*25)
print("     WELCOME TO TGB ATM     ")
print("-"*25)
print("Customer name: ",customer.name)
print("Customer Account: ",customer.account_no)                 
print("Date           : ",datetime.now().strftime("%d-%m-%y"))
print("-"*25)
while True:
    print("\n1.check balance:")
    print("2.deposit")
    print("3.withdraw")
    print("4.mini ststement")
    print("5.exit")
    choice=input("Enter the choice(1-4): ")
    if choice=="1":
        customer.check_balance()
    elif choice=="2":
        amount=int(input("Enter the amount: "))
        customer.deposit(amount)
    elif choice=="3":
        amount=int(input("Enter the amount: "))
        customer.withdraw(amount)
    elif choice=="4":
        customer.mini_statement()              
    elif choice=="5":
        print("----Thanks for choosing our ATM----")
        break
    else:
         print("it is invalid option")


