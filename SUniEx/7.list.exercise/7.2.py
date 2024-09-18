num1 = int(input())
num2 = int(input())

max_num = num2 * num1

output = list()

for i in range(num1, max_num + 1, num1):
    output.append(i)

print(output)