def positive_num(nums):
    return [str(i) for i in nums if i >= 0]
def negative_num(nums):
    return [str(i) for i in nums if i < 0]
def even_num(nums):
    return [str(i) for i in nums if i % 2 == 0]
def odd_num(nums):
    return [str(i) for i in nums if i % 2 != 0]


numbers = [int(i) for i in input().split(', ')]

print(f"Positive: {', '.join(positive_num(numbers))}")
print(f"Negative: {', '.join(negative_num(numbers))}")
print(f"Even: {', '.join(even_num(numbers))}")
print(f"Odd: {', '.join(odd_num(numbers))}")