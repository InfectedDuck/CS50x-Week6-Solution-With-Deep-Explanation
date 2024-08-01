while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 8.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Generate the pyramid
for i in range(1, height + 1):
    # Print the pyramid row by row
    print(' ' * (height - i) + '#' * i)
