text = input()
emotes = ''

for i in range(0, len(text)):
    if text[i] == ':':
        print(text[i] + text[i + 1])