class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    # debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs. " ,amount,"debited")
        print("The total amount now is: ",self.balance)

    # credit method
    def credit(self,amount):
        self.balance+=amount
        print("Rs. ",amount, "credited")
        print("The total amount now is: ",self.balance)

    # printing the balance
    def print_balance(self):
        print("the available balance for account number:",self.acc_no,"is: ",self.balance)

acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
