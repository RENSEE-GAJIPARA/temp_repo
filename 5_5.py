from abc import ABC, abstractmethod
#Q1
'''
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self,r):
        print(f"Area of circle is: {3.14*r*r}")

class Rectangle(Shape):
    def area(self, l, w):
        print(f"Area of rectangle is: {l*w}")

radius = int(input("Enter the radius of circle: "))
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

c = Circle()
r = Rectangle()

c.area(radius)
r.area(length, width)
'''

#Q2
'''
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def perimeter(self, r):
        self.r = r

    def area(self):
        print(f"Area of circle is: {3.14*self.r*self.r}")

class Rectangle(Shape):
    def perimeter(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print(f"Area of rectangle is: {self.l*self.w}")

radius = int(input("Enter the radius of circle: "))
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

c = Circle()
r = Rectangle()

c.perimeter(radius)
r.perimeter(length, width) 

c.area()
r.area()

# class new(Shape):
#     def perimeter(self):
#         print("This is for trial purpose...")

# n = new()
# n.perimeter()

#TypeError: Can't instantiate abstract class new without an implementation for abstract method 'area'
'''

#Q3
'''
class MLModel(ABC):
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass

class LinearRegressionMoodel(MLModel):
    def train(self):
        print("This is training phase of Linear Regression model")

    def predict(self):
        print("This is predicting phase of Linear Regression model\n")

class DecisionTreeModel(MLModel):
    def train(self):
        print("This is training phase of Decision Tree model")
    
    def predict(self):
        print("This is predicting phase of Decision Tree model")

models = [LinearRegressionMoodel(), DecisionTreeModel()]

for i in models:
    i.train()
    i.predict()
'''

#Q4
'''
class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class BankAccount(Account):
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited amount is: {amount}")
            print(f"New balance is : {self.__balance}")
        else: 
            print("Invalid amount...")

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            print(f"Withdrawn amount is: {amount}")
            print(f"Remaing balance is : {self.__balance}")
        else:
            print("Please check your balance...")

    def get_balance(self):
        return self.__balance
    
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_intrest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"{interest} intrest added.")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, limit):
        super().__init__(account_number, balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.limit:
            print(f"Withdran: {amount}")
            new_balance = self.get_balance() - amount
            self._BankAccount__balance = new_balance

        else:
            print("limit exceeded.")


print(f"{"="*20} Bnak Account Management System {"="*20}")

account_number = int(input("Enter your Account Number: "))
balance = float(input("Enter your balance: "))
interest_rate = float(input("Enter interest Rate: "))
deposite_amount = float(input("Enter your how many amount you want to deposite: "))
withdraw_amount = float(input("Enter your how many amount you want to withdraw: "))
limit = float(input("Enter overdraft limit: "))

s = SavingAccount(account_number, balance, interest_rate)
s.deposit(deposite_amount)
s.add_intrest()
print(f"Saving balance is: {s.get_balance()}")

c = CurrentAccount(account_number, balance, limit)
c.withdraw(withdraw_amount)
print(f"Current balance: {c.get_balance()}")
'''   