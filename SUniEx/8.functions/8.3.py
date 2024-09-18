action = input()
num1 = int(input())
num2 = int(input())


def solve():
    if action == "multiply":
        result = num1 * num2
    elif action == "add":
        result = num1 + num2
    elif action == "divide":
        result = num1 / num2
    elif action == "subtract":
        result = num1 - num2
    print(int(result))


solve()
