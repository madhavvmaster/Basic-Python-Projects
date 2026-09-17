try:
    num = int(input("Enter the number: "))

    if (num % 2 == 0):
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

except (ValueError, TypeError) as e:
    print(f"Error: {e}")                