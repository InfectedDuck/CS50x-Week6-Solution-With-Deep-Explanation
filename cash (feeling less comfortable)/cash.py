from cs50 import get_float
while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break
    else:
        print("Invalid input. Please enter a non-negative value.")
cents = round(change * 100)
quarters = 25
dimes = 10
nickels = 5
pennies = 1
num_coins = 0
num_coins += cents // quarters
cents %= quarters
num_coins += cents // dimes
cents %= dimes
num_coins += cents // nickels
cents %= nickels
num_coins += cents // pennies
print(num_coins)
