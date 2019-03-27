# 1.
while True:
    first_num = input("First number: ")
    second_num = input("Second number: ")
    operation = input("Choose operation: 0, +, -, *, / ")

    if operation == "0":
        print("Exiting...")
        break

    elif operation == "+":
        print(int(first_num) + int(second_num))

    elif operation == "-":
        print(int(first_num) - int(second_num))

    elif operation == "*":
        print(int(first_num) * int(second_num))

    elif operation == "/":
        print(int(first_num) / int(second_num))

    else:
        print("Wrong input")

# 2.


def numcheck(natural_num):
    even = 0
    odd = 0

    if natural_num == 0:
        return even, odd

    if natural_num % 2 == 0:
        even += 1
    else:
        odd += 1

    result = numcheck(natural_num // 10)
    even += result[0]
    odd += result[1]

    return even, odd


while True:
    input_num = int(input("Enter the integer: "))
    if input_num == 0:
        break
    print(numcheck(input_num))

# 3.


def reversenum(input_int):
    result = 0
    while input_int != 0:
        tail = input_int % 10
        input_int = input_int // 10
        result = result * 10 + tail
    return result


while True:
    n = int(input("Enter the integer: "))
    if n == 0:
        break
    print(reversenum(n))
