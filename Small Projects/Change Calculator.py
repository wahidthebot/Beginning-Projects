import decimal

change = decimal.Decimal(input("Enter the amount of change: "))
coins = 0

quarters = int(change // 0.25)
coins += quarters
change -= decimal.Decimal(quarters * 0.25)

dimes = int(change // 0.1)
coins += dimes
change -= decimal.Decimal(dimes * 0.1)

nickels = int(change // 0.05)
coins += nickels
change -= decimal.Decimal(nickels * 0.05)

if change > 0:
    coins += 1

print("Number of coins required:", coins)
