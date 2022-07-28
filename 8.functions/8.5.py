def buy(food, quantity):
    if food == 'coffee':
        price = 1.50
    elif food == 'coke':
        price = 1.00
    elif food == 'coke':
        price = 1.40
    elif food == 'coke':
        price = 2.00
    return price * quantity


print(buy(input(), input()))
