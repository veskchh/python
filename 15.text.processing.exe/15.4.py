def encrypt(word):
    new_word = ''
    for i in word:
        new_word += chr(ord(i) + 3)
    return new_word

string = input()


print(encrypt(string))