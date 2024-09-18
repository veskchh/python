first_list = input().split(", ")
second_list = input().split(", ")
substrings = []

for word in first_list:
    for words in second_list:
        if word in words and word not in substrings:
            substrings.append(word)

print(substrings)