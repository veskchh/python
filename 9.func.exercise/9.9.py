def pass_checker(password):
    digit_count = 0
    global osem
    global digits_req
    osem = True
    digits_req = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        osem = False
    all_ok_check = password.isalnum()
    for n in password:
        if n.isdigit():
            digit_count += 1
    if digit_count < 2:
        digits_req = False
    if not all_ok_check:
        print('Password must consist only of letters and digits')
    if not digits_req:
        print('Password must have at least 2 digits')
    if osem and all_ok_check and digits_req:
        print('Password is valid')


password_try = input()

pass_checker(password_try)
