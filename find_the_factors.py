#Assignment: Find the factors of a number p81

number = int(input("Enter a positive integer: "))

for num in range(1, 100):
    if number % num == 0:
        print(f"{num} is a divisor of {number}")
