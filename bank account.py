class BankAccount:
    def __init__(self,name,accno,balance=0):
        self.name = name
        self.accno = accno
        self.balance = balance
        print("Account created successfully")
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited succesfully\nBalance: ",self.balance)
        else:
            print("Amount must be a positive number")
    def withdrawel(self,amount):
        if amount <= 0:
            print("Amount must be a positive number")
        elif amount < self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount withdrew successfully!\nBalance: ",self.balance)
    def display(self):
        print("Account Details")
        print("Account Holder: ",self.name)
        print("Account Number: ",self.accno)
        print("Current Balance: ",self.balance)

print("Welcome to simple Bank System")
name = input("Enter account holder name: ")
accno = input("Enter account name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name,accno,balance)

while True:
    print("Account Operations")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Display")
    print("4.Exit")
    print("Enter your choice: ")
    