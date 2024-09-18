n = int(input())

positives = list()
negatives = list()

for x in range(n):
    num = int(input())
    if num < 0:
        negatives.append(num)
    else:
        positives.append(num)

positives_count = len(positives)
negatives_sum = sum(negatives)

print(positives)
print(negatives)


print(f'Count of positives: {positives_count}')
print(f'Sum of negatives: {negatives_sum}')
