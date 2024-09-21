from operations.plus import plus
from operations.minus import minus
from operations.multy import multy
from operations.divide import divide

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
operation = input("+, -, * or /: ")

result = 0

if operation == "+":
    result = plus(num1, num2)
elif operation == "-":
    result = minus(num1, num2)
elif operation == "*":
    result = multy(num1, num2)
elif operation == "/":
    result = divide(num1, num2)

print((f"Result is {result}"))