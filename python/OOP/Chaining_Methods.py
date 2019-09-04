class User:
    def __init__(self, first, last, email, password, age, gender, account_balance):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.password = password
        self.age = int(age)
        self.gender = gender
        self.account_balance = account_balance
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        print("Your Updated Balance is: ", (self.account_balance))
        return self
    def make_deposit(self, amount):
        self.account_balance += amount
        print("Your Updated Balance is: ", (self.account_balance))
        return self
    def transfer_money(self, other, amount):
        if self.account_balance < amount:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            other.account_balance += amount
        print("You just transfered {} to {}'s account!".format(amount, other.first_name))
        print("{}'s account balance was reduced to: {}".format(self.first_name, self.account_balance))
        return self





jeremy = User('Jeremy', 'Grey', 'ThisIsSparta@gmail.com', 'mypassword', 38, 'male', 222)
kathryn = User('Kathryn', 'James', 'HiImKat@yahoo.com', 'jinglebells', 28, 'female', 888)
finding = User('Finding', 'Nemo', 'ImAFish@fishspace.com', 'CurrentDrifter12', 9, 'self-replicating', 938381840)

jeremy.make_deposit(64).make_deposit(83).make_deposit(12).make_withdrawl(194)

kathryn.make_deposit(938).make_deposit(8138).make_withdrawl(333).make_withdrawl(888)

finding.transfer_money(jeremy, 830183).make_deposit(1337).make_withdrawl(80085).make_withdrawl(1134).make_withdrawl(7145)
