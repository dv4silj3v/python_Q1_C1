# 4.
n = int(input("n = "))
result = -2
sum_row = 0
for k in range(0, n):
    result = result*(-0.5)
    sum_row += result

print(sum_row)

# 5.
n = 32
delimeter = " "
while n < 128:
    if n > 99:
        delimeter = ""
    print(f"| {n}{delimeter} — {chr(n)}", end="")

    n += 1
    if n % 10 == 2:
        print(" |")

# 6.
import random

n = 0
number = random.randint(0, 100)

print("Try to guess number from 0 to 100, you have 10 attempts!")
while n < 10:
    choice = int(input(f"Attempt #{n+1}: "))
    if choice == number:
        print("Correct!")
        exit(0)
    elif number < choice:
        print("Number is smaller")
    elif number > choice:
        print("Number is bigger")

    n += 1


print(f"You lose, number is {number}")

