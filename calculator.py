class Calculator:
    def add(self,num1,num2):
        return num1 + num2
    def subtract(self,num1,num2):
        return num1 - num2
    def divide(self,num1,num2):
        return num1 / num2
    def multiply(self,num1,num2):
        return num1 * num2

test = Calculator()

print(test.add(1,3))
print(test.subtract(5,1))
print(test.divide(4,2))
print(test.multiply(5,2))