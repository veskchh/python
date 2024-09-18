n = int(input())
word = str(input())
list_of_words = list()

for i in range(n):
    list_of_words.append(input())

print(list_of_words)

for i in range(len(list_of_words) - 1, -1, -1):
    if word not in list_of_words[i]:
        list_of_words.remove(list_of_words[i])

print(list_of_words)