from practise import Bank, Customer, Staff
import sys
import json

class BankFactory():
    @staticmethod
    def create_bank_entry(detail,name,address,**kwargs):
        if detail.lower() == 'staff':
            return Staff(name,address,**kwargs)
        elif detail.lower() == 'customer':
            return Customer(name,address,**kwargs)
        else:
            print("Invalid detail! Please choose either 'staff' or 'customer'.")

def main():
    detail = sys.argv[1]
    name = sys.argv[2]
    address = sys.argv[3]
    args = sys.argv[4:]

    input = {}
    for arg in args:
        key,value = arg.split("=")
        input[key]=value

    entry = BankFactory.create_bank_entry(detail,name,address,**input)



    entry.deposit(2200)
    entry.withdraw(300)
    receiver = Customer('Milan','KTM')
    entry.transfer(200,receiver)

    data = {
        entry.id: {'name': entry.name,'address': entry.address,'balance': entry.balance,'status': entry.status
        }
    }

    with open(f'{detail}.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()