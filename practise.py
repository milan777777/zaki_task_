import json
from abc import abstractmethod, ABC
class Bank(ABC):
    bank_name = 'Nabil Bank'
    def __init__(self, name, address, pin = 1234, balance = 0):
        self.id = id(self)
        self.name = name
        self.address = address
        self.__pin = pin
        self.balance = balance 
        self.status = 'active'

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    
    def check_datatype(data_type):
        def validate(func):
            def wrapper(*args):
                if not isinstance(args[1],data_type):
                    print(f"Invalid datatype. Datatype should be {data_type}")
                    return False
                return func(*args)
            return wrapper
        return validate

    def validate_balance(func):
        def wrapper(self, amount, *args):
            if self.balance < amount:
                print("Sorry, this transaction cannot be held.")
                print(f"Insufficient balance : Rs.{self.balance}.")
                return False
            return func(self,amount, *args)
        return wrapper
    
    def change_pin(self, old_pin, new_pin):
        if self.__pin != old_pin:
            print("Incorrect old PIN. PIN change failed.")
        else:
            self.__pin = new_pin
            print(f"Dear {self.name}, your PIN has been changed successfully.")


class Customer(Bank):
     def __init__(self, name, address, pin=1234, balance=0):
         super().__init__(name, address, pin, balance)

     @Bank.check_datatype(int)
     def deposit(self, amount):
         print(f"Dear {self.name},Rs {amount} has been deposited to your {Bank.bank_name}")
         self.balance += amount
         print(f"Total Balance : Rs.{self.balance}")
         
     @Bank.check_datatype(int)
     @Bank.validate_balance
     def withdraw(self, amount):
         print(f"Dear {self.name}, Rs {amount} has been withdrawn from your{Bank.bank_name}") 
         self.balance -= amount
         print(f"Total Balance : Rs{self.balance}")

     @Bank.check_datatype(int)
     @Bank.validate_balance
     def transfer(self, amount, receiver):
         self.balance -= amount
         Staf.balance += amount
         print(f"Dear {receiver}, Rs {amount} has been transferred to your {Bank.bank_name}")

class Staff(Bank):
    def __init__(self, name, address,department , pin=1234, balance=0):
        super().__init__(name, address, pin, balance)
        self.department = department

    @Bank.check_datatype(int)
    def deposit(self,amount):
        print(f"Dear {self.name}, Rs {amount} has been deposited to your {Bank.bank_name}")
        self.balance += amount
        print(f"Total Balance : Rs{self.balance}")

    @Bank.check_datatype(int)
    @Bank.validate_balance
    def withdraw(self,amount):
        print(f"Dear {self.name}, Rs {amount} has been withdrawn from your account {Bank.bank_name}")
        self.balance -= amount
        print(f"Total Balance : Rs{self.balance}") 

    @Bank.check_datatype(int)
    @Bank.validate_balance
    def transfer(self, amount, receiver):
        self.balance -= amount
        Staf.balance += amount
        print(f"Dear {receiver}, Rs {amount} has been transferred to your {Bank.bank_name}")

Cust = Customer('Milan', 'Kathmandu', 1234, 100000)
Staf = Staff('Ram', 'Sanepa', 'Manager', 1234, 150000)
Cust.change_pin(1234, 5432)
Staf.change_pin(1234,3213)
Cust.deposit(1500)       
Staf.deposit(2000)
Cust.withdraw(200000)
Staf.withdraw(30000)
Cust.transfer(15000, Staf.name)
Staf.transfer(20000,Cust.name)

data = {}
data[Cust.id] = {'name':Cust.name, 'address':Cust.address,'balance':Cust.balance}
with open('customer.json','w') as f:
    json.dump(data, f, indent=4)

data = {}
data[Staf.id] = {'name':Staf.name, 'address':Staf.address, 'department':Staf.department, 'balance':Staf.balance}
with open('staff.json','w') as f:
    json.dump(data, f, indent=4)


      
        

         
     
            

        