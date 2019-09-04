class BankAccount:
    def __init__(self, user, pw, TH):
        self.userid = user
        self.password = pw
        self.balance = 5
        self.interest_rate = 0.01
        self.transaction_history = TH
    def deposit(self, amount):
        self.balance += amount
        print("Your updated account balance is: ${}".format(self.balance))
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = self.balance - 5
            print("Insufficient funds. Charging a $5 fee.")
            print("Your balance is now: ${}".format(self.balance))
        else:
            self.balance -= amount
            print("Your updated account balance is: ${}".format(self.balance))
        return self
    def display_account_info(self):
        print("Balance: {}".format(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            print("Balance before interest gained: ${}".format(self.balance))
            self.balance = self.balance + self.balance * self.interest_rate
            print("Balance after interest gained: ${}".format(self.balance))
        elif self.balance < 0:
            print("Consider adding funds to your bank account.")
        return self


jeremy = BankAccount('jeremyuser', 'password', 'you have been spending way too much money on your yet-to-be-married partner')
kathryn = BankAccount('kathrynusername', 'mypassword', 'you have saved overall too much money, you should go spend some')

jeremy.deposit(4.88).deposit(8.3).deposit(5.1).withdraw(333.33).yield_interest()
kathryn.deposit(9999.99).deposit(12455.55).withdraw(5.55).withdraw(15).withdraw(12).withdraw(3.50).yield_interest()