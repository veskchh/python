import sys

sum_all = 0
min = sys.maxsize
max = -sys.maxsize
numbers = list(input().split())

for i in numbers:
    a = int(i)
    sum_all += a
    if a < min:
        min = a
    if a > max:
        max = a

print(f"The minimum number is {min}")
print(f"The maximum number is {max}")
print(f"The sum number is: {sum_all}")