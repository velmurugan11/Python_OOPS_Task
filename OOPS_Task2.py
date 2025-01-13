# OOPS SIMPLER TASKS
# Task1
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def introduce(self):
        return f"Introducing {self.name}"

P1 = person("vel",22)
print(P1.introduce())

# Task2
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def start(self):
        print("The car has started")
P2 = Car("Ford","Black")
P2.start()

# Task3
class student:
    def __init__(self,name,grade=[0,0,0,0,0]):
        self.name=name
        self.grade=grade
    def avg(self):
        Marks=self.grade
        Avg=0
        for i in Marks:
            Avg+=i
        Avg//=5
        return f"{self.name} is obtained the average of {Avg}"
P3=student("vel",[29,71,80,81,69])
print(P3.avg())

# Task4
class Rectangle:
    def __init__(self,length,breadth):
        self.len=length
        self.breadth=breadth
    
    def area(self):
        return f"Area of Rectangle is {self.len*self.breadth}"
    def perimeter(self):
        return f"Perimeter of Rectangle is {(self.len+self.breadth)*2}"

R = Rectangle(20,10)
print(R.area(),R.perimeter())

# Task5
class Bank_Account:
    def __init__(self,account_number,Current_balance):
        self.account_number=account_number
        self.__balance=Current_balance
    
    def get_balance(self):
        return self.__balance

    def deposit(self):
        Amount = int(input("Enter the amount to deposit: "))
        Current_Balance = self.__balance
        New_Balance = Amount+Current_Balance
        self.balance = New_Balance
        return f"Balance before the deposit {Current_Balance} , Balance after the deposit {New_Balance}"
    
    def withdraw(self):
        Amount=int(input("Enter the Amount to Withdraw: "))
        Current_Balance = self.__balance
        if Amount>Current_Balance:
            return f"Low Balance"
        else:
            New_Balance = Current_Balance-Amount
        self.balance = New_Balance
        return f"Balance after the Withdrawal {New_Balance}"
B1 = Bank_Account(3824890033,2000)
print(f"Current_Balance:{B1.get_balance()}")

print(B1.deposit())
print(B1.withdraw())
print(B1.get_balance())

# Task6
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print ("The dog barks")
class Cat(Animal):
    def speak(self):
        print ("The Cat Meow")

Dog().speak()
Cat().speak()

# Task7
class Employee:
    def __init__(self,name,position,salary):
        self.__name=name
        self.__position=position
        self.__salary=salary
    
    
    def display_info(self):
        print(f"Employee Name: {self.__name}")
        print(f"Employee Position: {self.__position}")
        print(f"Employee salary: {self.__salary}")

Name=input("Enter The Name:")
Position=input("Enter The Position:")
Salary=input("Enter The Salary:")
Employee1=Employee(Name,Position,Salary)
Employee1.display_info()
