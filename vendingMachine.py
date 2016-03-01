
coins = [100, 50, 20, 10, 5]

def give_change(amount):
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
        if amount == 3:
            change.append(coins[-1])

    return change

amount = input("enter amount")
change = give_change(amount)
print change
