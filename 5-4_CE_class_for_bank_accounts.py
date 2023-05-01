

class Account:
    def __init__(self, name):
        self.balance = 0    # bakiye
        self.overdraft = 100 # kredili mevduat hesabı
        self.interest_positive = 0.01
        self.interest_negative = 0.10
        self.withdraw_rate = 0.001
        self.name = name

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, withdraw_amount):
        if self.balance + self.overdraft >= withdraw_amount:
            self.balance -= withdraw_amount
        else:
            print('Balance is not sufficient!')
        return  self.balance

    def add_interest(self):
        if self.balance >= 0:
            interest = self.balance * self.interest_positive
        else:
            interest = self.balance * self.interest_negative
        self.balance += interest
        return self.balance

class CreditAccount(Account):
    def __init__(self):
        Account.__init__(self, 'credit_name')
        self.interest_negative = 0.05

    def withdraw_money(self, amount):
        amount_withdraw = amount + amount * self.withdraw_rate
        if amount_withdraw <= self.balance + self.overdraft:
            self.balance -= amount_withdraw
        else:
            print('Balance is not sufficient!')
        return self.balance

    def set_overdraft_limit(self, limit):
        self.overdraft = limit


asd = Account('aliveli2')
asd.deposit(120)
#asd.withdraw(18)
print(asd.name)
#myfirstaccount = CreditAccount()
#myfirstaccount.deposit(220)
#(print(myfirstaccount.withdraw_money(100)))