def numbers(first, second):
    symbols = list()
    for i in range(ord(first) + 1, ord(second)):
        symbols.append(chr(i))
    return symbols


char1 = input()
char2 = input()
result = numbers(char1, char2)
for i in result:
    print(i, end=" ")




