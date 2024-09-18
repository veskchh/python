def length(username):
    if 3 <= len(username) <= 16:
        return True


def type_of_symbols(username):
    for char in username:
        if not (char.isalnum() or char == '_' or char == "-"):
            return False
    return True


def redundant(username):
    for character in username:
        if character == ' ':
            return False
    return True


def user_valid(username):
    if length(username) and type_of_symbols(username) and redundant(username):
        return True


usernames = input().split(", ")
for user in usernames:
    if user_valid(user):
        print(user)


