import random

choices = ["rock", "paper", "scissors"]
user = input("Enter rock, paper or scissors: ")
computer = random.choice(choices)

print(f"You chose: {user}")
print(f"Computer chose: {computer}")

if user == computer:
    print("\nIt's a draw!\n")
elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
    print("\nYou won!\n")
elif (user == "scissors" and computer == "rock") or (user == "rock" and computer == "paper") or (user == "paper" and computer == "scissors"):
    print("\nYou lose!\n")
else:
    print("\nInvalid Input!\n")