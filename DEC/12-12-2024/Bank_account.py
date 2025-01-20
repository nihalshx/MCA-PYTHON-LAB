"""
Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
"""


class BankAccount:
    def __init__(self,id,name,acc_type,balance):
        self.id = id
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
    def deposit(self):
        amount = float(input("Enter Amount to deposit: "))
        self.balance += amount
        print(f"New Balance is {self.balance}\n")
    
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance > amount:
            self.balance -= amount
            print(f'New Balance after withdrawing is: {self.balance}\n')

        else:
            print("Not sufficient balance")
            print(f'Balance: {self.balance}')
            
    def display(self):
        id = self.id 
        name = self.name
        acc_type = self.acc_type
        balance = self.balance 
        print(f'Hello, Mr.{name}\nYour id is {id}\nAccount Type: {acc_type}\nBalance:{balance}')
        
        
id = 200
name = "Steven Smith"
acc_type  = "Savings"
obj1 = BankAccount(id,name,acc_type,balance = 78016)
obj1.display()
obj1.deposit()
obj1.withdraw()
obj1.display()