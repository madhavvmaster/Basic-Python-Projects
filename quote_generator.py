import random

quotes = ["Life isn't about finding yourself. Life is about creating yourself.",
          "You can't cross the sea merely by standing and staring at the water.",
          "Whether you think you can or think you can't, you're right.",
          "The best time to plant a tree was 20 years ago. The second best time is now.",
          "I am not a product of my circumstances. I am a product of my decisions.",
          "Success is the sum of small efforts, repeated day-in and day-out.",
          "Success is not final; failure is not fatal: It is the courage to continue that counts.",
          "It is not in the stars to hold our destiny but in ourselves.",
          "Doubt kills more dreams than failure ever will.",
          "Strive not to be a success, but rather to be of value."]

quote = random.choice(quotes)
print(f"Random Quote: {quote}")