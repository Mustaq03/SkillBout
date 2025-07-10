class Calculator:
    def __init__(self,num1,num2 ):
        self.num1 = num1
        self.num2 = num2
    def multiply(self,num1,num2):
        return num1*num2
    def divide(self,num1,num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    def add(self,num1,num2):
        return num1+num2
    def subtract(self,num1,num2):
        return num1-num2
num1,num2=map(int,input().split())
c=Calculator(num1,num2)
print(f"Addition ({num1}+{num2}) : {c.add(num1,num2)}")
print(f"Subtraction ({num1}{num2} ): {c.subtract(num1,num2)}")
print(f"Multiplication ({num1}*{num2}) : {c.multiply(num1,num2)}")
print(f"Division ({num1}/{num2}) : {c.divide(num1,num2)}")