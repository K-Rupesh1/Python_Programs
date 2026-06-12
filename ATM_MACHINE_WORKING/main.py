password=1361
balance=10000
pin=int(input("enter your pin : "))
if pin!=password:
    print("you have entered wrong pin")
else:
    print("1.balance enquiry")
    print("2.amount withdrawl")
    print("3.change pin")
    user_input=int(input("select your choice : "))
    if user_input==1:
        print(f"your account balance is : {balance} ")
    elif user_input==2:
        print("1.savings account")
        print("2. current account")
        print("3. salary account")
        user=int(input("select your account type : "))
        if user==1:
            amount=int(input("enter amount : "))
            if amount<=balance:
                print("withdrawl successfully completed")
                balance-=amount
                print(f"your remaining balance : {balance}")
            else:
                print("you have entered wrong amount")
        elif user==2:
            amount=int(input("enter amount : "))
            if amount<=balance:
                balance-=amount
                print(f"your remaining balance : {balance}")
            else:
                print("you have entered wrong amount")
        else:
            amount=int(input("enter amount : "))
            if amount<=balance:
                balance-=amount
                print(f"your remaining balance : {balance}")
            else:
                print("Insufficient Amount")
    elif user_input==3:
        print("please contact your branch ")
    else:
        print("invalid input")
    
# BY USING FUNCTIONS
password=1361
balance=10000
count=3
def User_Input():
    pin=int(input("enter your pin : "))
    return pin
    
def Check_Balance():
    print(f"your balance {balance}")
def Withdraw_Amount():
    global balance
    if not Select_Account_type():
        return 
    amount=int(input("enter amount : "))
    if amount<=balance:
        print("withdraw successfull")
        balance-=amount
        print(f"remaining balance {balance}")
    else:
        print("Insufficient Amount")
        return False
def Select_Account_type():
    print("1.savings account")
    print("2.current account")
    print("3.salary account")
    user=int(input("select your account type : "))
    if user==1:
        print("savings account seleted")
        return True
    elif user==2:
        print("current account selected")
        return True
    elif user==3:
        print("salary account selected")
        return True
    else:
        return False
def main():
   
    pin=int(input("enter your pin : "))
    if pin==password:
        print("1.balance enquiry")
        print("2.amount withdraw")
        select=int(input("choose type :"))
        if select==1:
            return Check_Balance()
        else:
            return Withdraw_Amount()
    else:
        print("password incorrect")
        global  count
        count-=1
        print(f"your remaining attempts : {count}")
        return User_Input()     
if __name__ == "__main__":
    main()
            
            
# BY USING CLASS:
class ATM:
    def __init__(self, password, balance):
        self.password = password
        self.balance = balance
    def check_pin(self):
        pin = int(input("Enter your pin: "))

        if pin == self.password:
            return True
        else:
            print("Password incorrect")
            return False
    def check_balance(self):
        print(f"Your balance is {self.balance}")
    def select_account_type(self):
        print("1. Savings account")
        print("2. Current account")
        print("3. Salary account")

        user = int(input("Select your account type: "))

        if user == 1:
            print("Savings account selected")
            return True
        elif user == 2:
            print("Current account selected")
            return True
        elif user == 3:
            print("Salary account selected")
            return True
        else:
            print("Invalid account type")
            return False
    def withdraw_amount(self):
        if not self.select_account_type():
            return

        amount = int(input("Enter amount: "))

        if amount <= self.balance:
            print("Withdraw successful")
            self.balance -= amount
            print(f"Remaining balance: {self.balance}")
        else:
            print("Insufficient balance")
    def menu(self):
        print("1. Balance enquiry")
        print("2. Amount withdraw")

        select = int(input("Choose type: "))

        if select == 1:
            self.check_balance()
        elif select == 2:
            self.withdraw_amount()
        else:
            print("Invalid choice")
    def run(self):
        if self.check_pin():
            self.menu()
atm = ATM(1361, 10000)
atm.run()
        

