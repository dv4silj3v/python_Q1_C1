import random

# 1.
number = int(input("Please enter the 3-digit number: "))
if len(str(number)) == 3:
    a = number // 100
    b = (number - (a * 100)) // 10
    c = number - (a * 100) - (b * 10)
    print("Sum of digits = ", a + b + c)
    print("Multiplication of digits = ", a * b * c)
else:
    print("Incorrect 3-digit number")

# 2.
d = 5
e = 6
print("Binary AND result: ", d & e)
print("Binary OR result: ", d | e)
print("Binary XOR reult: ", d ^ e)
print("Binary Ones Complement: ", ~d)
print("Binary left shift of number 5: ", d << 2)
print("Binary right shift of number 5: ", d >> 2)
# Битовый сдвиг вправо на n равносилен целочисленному делению на 2^n и наоборот.

# 3.

x1 = int(input("Please enter x1: "))
y1 = int(input("Please enter y1: "))
x2 = int(input("Please enter x2: "))
y2 = int(input("Please enter y2: "))
k = (y2 - y1)/(x2 - x1)
b = y2 - k * x2
print("Linear function is: y = {}x + {}".format(k, b))

