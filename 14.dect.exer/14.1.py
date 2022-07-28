string = input().split()
letters = {}
for i in string:
    for x in i:
        if x not in letters:
            letters[x] = 1
        else:
            letters[x] += 1

for k, v in letters.items():
    print(f"{k} -> {v}")