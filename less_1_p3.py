# 7.
a = int(input("Enter side A of triangle: "))
b = int(input("Enter side B of triangle: "))
c = int(input("Enter side C of triangle: "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle is Valid")
    if a == b == c:
        print("Triangle is equilateral")
    elif a == b or b == c or c == a:
        print("Triangle is isosceles")
    else:
        print("Triangle is scalene")
else:
    print("Triangle is Invalid")

# 8.
year = int(input("Enter the year: "))
if year % 4 != 0:
    print("Year is usual")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Leap year!!")
    else:
        print("Year is usual")
else:
    print("Leap year!!")

# 9.
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if c < a < b or b < a < c:
    print("Number in the middle is: ", a)
elif c < b < a or a < b < c:
    print("Number in the middle is: ", b)
elif a == b or b == c or a == c:
    print("All numbers must be different!!")
else:
    print("Number in the middle is: ", c)

