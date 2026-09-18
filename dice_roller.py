import random

def roll_dice():
    return random.randint(1, 6)

print("Welcome to Dice Roller!!!")
num_dice = int(input("Enter how many times you want to roll the dice: "))

for i in range(num_dice):
    print(f"Dice {i + 1}: {roll_dice()}")