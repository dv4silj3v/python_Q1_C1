import random

# 4.
a = int(input("Enter the lower bound of a random integer: "))
b = int(input("Enter the upper bound of a random integer: "))
print("Random number is: ", random.randint(a, b))

c = float(input("Enter the lower bound of a random float: "))
d = float(input("Enter the upper bound of a random float: "))
print("Random number is: ", random.uniform(c, d))

e = input("Enter the lower bound of a random letter: ")
f = input("Enter the upper bound of a random letter: ")
print(chr(random.choice(range(ord(e), ord(f)))))

# 5.
g = input("Enter the lower bound of a random letter: ")
h = input("Enter the upper bound of a random letter: ")

print("Position of the lower letter: ", ord(g) - 96)
print("Position of the upper letter: ", ord(h) - 96)
print("{} letters between '{}' and '{}'".format(ord(h) - ord(g), g, h))

# 6.

i = int(input("Enter the letter position: "))
if 0 < i <= 26:
    print(chr(i + 96))
else:
    print("Incorrect letter position, please enter number between 1 and 26")
