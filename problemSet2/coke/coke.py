total = 50

while total > 0: 
    print("Amount Due:", total)
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        total -= coin

print("Change Owed:", -total)
