import random

number = random.randint(1, 101)
attempts = 0

print("Welcome to Number Guessing Game!!!")
print("I'm thinking a number between 1 to 100.")

while True:
    try:
        guess = int(input("Enter the guessed number: "))
        attempts += 1
    except (ValueError, TypeError) as e:
        print(f"Error: {e}. So try again with valid integer value.")
        continue

    if guess == number:
        print(f"You guessed the correct number in {attempts} attempts.")
        break
    elif guess > number:
        print(f"The number is too high so try guessing lower number.")
    elif guess < number:
        print(f"The number is too low so try guessing higher number.")
    else: 
        print(f"The number you guessed is out of range. Try again within 1 to 100.")
