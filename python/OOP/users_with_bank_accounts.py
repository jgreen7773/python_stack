class User:
    def __init__(self, first, last, email, password, age, gender, account):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.account = BankAccount(balance=5, interest_rate=0.02)
    def make_withdrawl(self, amount):
        self.account -= amount
        print("Your Updated Balance is: ${}".format(self.account))
    def make_deposit(self, amount):
        self.account += amount
        print("Your Updated Balance is: ${}".format(self.account))
    def transfer_money(self, other, amount):
        if self.account < amount:
            print("Insufficient funds.")
        else:
            self.account -= amount
            other.account += amount
        print("You just transfered ${} to {}'s account!".format(amount, other.first_name))
        print("{}'s account balance was reduced to: ${}".format(self.first_name, self.account))


class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = 5
        self.interest_rate = 0.02
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
            self.balance = self.balance + self.balance * float(self.interest_rate)
            print("Balance after interest gained: ${}".format(self.balance))
        elif self.balance < 0:
            print("Consider adding funds to your bank account.")
        return self

jeremy = User('Jeremy', 'Grey', 'ThisIsSparta@gmail.com', 'mypassword', 38, 'male', 888)
kathryn = User('Kathryn', 'James', 'HiImKat@yahoo.com', 'jinglebells', 28, 'female', 333)
finding = User('Finding', 'Nemo', 'ImAFish@fishspace.com', 'DriftingCurrents12', 9, 'self-replicating', 1839146)

kathryn.account.deposit(9999.99).deposit(12455.55).withdraw(5.55).withdraw(15).withdraw(12).withdraw(3.50).yield_interest()

finding.transfer_money(jeremy, 830183)
finding.make_deposit(1337)
finding.make_withdrawl(80085)
finding.make_withdrawl(1134)
finding.make_withdrawl(7145)