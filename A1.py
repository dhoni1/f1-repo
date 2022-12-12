# print("Welcome to HDFC Bank")

# A_Name = "Shaik Ameervali"

# print("Welcome to the HDFC Bank Mr.",A_Name)

# Amount = int(input("enter the Amount : "))
# Balance = print("Remaining Balance in the HDFC Bank",Amount)
# debit_amount = int(input("enter the amount"))
# Balance = Balance - debit_amount
# print(Balance)




# def function_creator():

# 	# expression to be evaluated
# 	expr = input("Enter the function(in terms of x):")

# 	# variable used in expression
# 	x = int(input("Enter the value of x:"))

# 	# evaluating expression
# 	y = eval(expr)

# 	# printing evaluated result
# 	print("y =", y)


# if __name__ == "__main__":
# 	function_creator()



'''class New_Account:
    B_name = "HDFC Bank"
    def __init__(self):
        self.account_no = eval(input("Enter the Account number :"))
        self.balance = eval(input("enter the starting ammount : "))
    def Deposit(self):
        deposit = eval(input("deposit amount : "))
        self.balance = self.balance + deposit
    def Withdraw(self):
        w = eval(input("Withdraw amount : "))
        self.balance = self.balance - w
    def check_balance(self):
        print(f"The Account number is {self.account_no} remaining amount is {self.balance}")

    print("welcome to ",B_name)
a = New_Account()
a.check_balance()
a.Deposit()
a.check_balance()
a.Withdraw()
a.check_balance()'''


# class test:
#     def __init__(self):
#         print("instructor")
#     def __del__(self):
#         print("destructor")

# a = test()
# a1 = test()
# a2 = test()
# a = test()
# del a1
# del a2


# class test2:
#     """document"""
#     x=100
#     def fun(self):
#         print("hello world")


# print(test2.__doc__)
# print(test2.__name__)
# print(test2.__module__)
# print(test2.__bases__)
# print(test2.__dict__)



# class test3:
#     a = 10
#     def fun(self):
#         self.b = 20
#         c = 30
#         print(test3.a)
#         print(self.b)
#         print(c)

# t1 = test3()
# t1.fun()
# test3.x = 100
# t1.y = 101

# t2 = test3()
# t2.fun()
# print(test3.x)
# print(t1.y)



# class X:
#     a = 100
#     def fun1(self):
#         self.b = 200
#         print(X.a)
#         print(self.b)

# class Y:
#     c = 300
#     def fun2(self):
#         self.d = 400
#         print(X.a)
#         x1 = X()
#         x1.fun1()
#         print(x1.b)
#         print(Y.c)
#         print(self.d)

# y1 = Y()
# y1.fun2()
import tet
print(tet.x)
print(tet.y)
tet.add(10,20)
t2 = tet.Test()
t2.sub(10,20)



