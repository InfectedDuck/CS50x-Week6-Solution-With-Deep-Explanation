from cs50 import get_float

# Continuously prompt the user for input until a valid non-negative value is provided
while True:
    # Get the amount of change owed from the user as a float
    change = get_float("Change owed: ")
    
    # Check if the provided change amount is non-negative
    if change >= 0:
        # Exit the loop if a valid input is received
        break
    else:
        # If the input is invalid (negative), prompt the user again
        print("Invalid input. Please enter a non-negative value.")

# Convert the amount of change from dollars to cents, rounding to the nearest whole number
cents = round(change * 100)

# Define the values of the different coin denominations in cents
quarters = 25  # Value of one quarter in cents
dimes = 10     # Value of one dime in cents
nickels = 5    # Value of one nickel in cents
pennies = 1    # Value of one penny in cents

# Initialize a counter to keep track of the total number of coins used
num_coins = 0

# Calculate the number of quarters needed and update the remaining cents
num_coins += cents // quarters  # Use integer division to determine the number of quarters
cents %= quarters  # Update the remaining cents after using quarters

# Calculate the number of dimes needed and update the remaining cents
num_coins += cents // dimes  # Use integer division to determine the number of dimes
cents %= dimes  # Update the remaining cents after using dimes

# Calculate the number of nickels needed and update the remaining cents
num_coins += cents // nickels  # Use integer division to determine the number of nickels
cents %= nickels  # Update the remaining cents after using nickels

# Calculate the number of pennies needed
num_coins += cents // pennies  # Use integer division to determine the number of pennies

# Output the total number of coins needed to make the change
print(num_coins)
