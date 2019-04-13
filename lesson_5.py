####### 1.
import random
from collections import defaultdict
from collections import deque


def company_generator(n):
    """
    This function will generate a list of companies with revenue by quarter.
    :param n: number of companies to generate
    :return: defaultdict
    """

    company_report = defaultdict(lambda: [0, 0, 0, 0])

    # We are going to use "/usr/share/dict/words" file for Company Name Generator
    with open('/usr/share/dict/words', 'r', encoding='UTF-8') as f:
        words = f.readlines()
    words = [x.strip() for x in words]

    # Generate revenue for each company and each quarter
    while n > 0:
        company_name = random.choice(words)
        company_report[company_name] = [random.randrange(10000, 100000), random.randrange(10000, 100000),
                                        random.randrange(10000, 100000), random.randrange(10000, 100000)]
        n -= 1

    return company_report


n = int(input("Please enter number of companies: "))
report = company_generator(n)
avg_revenue = 0
sum = 0

for revenue_values in report.values():
    for items in revenue_values:
        sum = sum + items
avg_revenue = sum / (n * 4)

print(avg_revenue)

for company in report:
    sum = 0
    for items in report[company]:
        sum = sum + items
    sum_avg = sum / 4
    if sum_avg > avg_revenue:
        print("Company {} has {} revenue, it's higher than average".format(company, sum_avg))
    else:
        print("Company {} has {} revenue, it's lower than average".format(company, sum_avg))






############ 2.

first_num = input("Please enter first number in a hexadecimal format: ")
second_num = input("Please enter second number in a hexadecimal format: ")
first_num_list = deque(first_num)
second_num_list = deque(second_num)

try:
    first_num_dec = int(first_num, 16)
    second_num_dec = int(second_num, 16)
except ValueError as e:
    print(e)


def sum_hex(a, b):
    a_dec = int(a, 16)
    b_dec = int(b, 16)
    sumnum = a_dec + b_dec
    sum_num_list = deque(hex(sumnum)[2:])
    return list(sum_num_list)


def mult_hex(a, b):
    a_dec = int(a, 16)
    b_dec = int(b, 16)
    multnum = a_dec * b_dec
    mult_num_list = deque(hex(multnum)[2:])
    return list(mult_num_list)


while True:
    print("-------------------------------")
    print("First number is: {}".format(list(first_num_list)))
    print("Second number is: {}".format(list(second_num_list)))
    print("Program has following options: ")
    print("1. Summarize ")
    print("2. Multiply ")
    print("3. Quit ")
    choice = input("Enter your choise [1-3]: ")
    if choice == "1":
        print("Sum of hex numbers = {}".format(sum_hex(first_num, second_num)))
    elif choice == "2":
        print("Multiply of hex number = {}".format(mult_hex(first_num, second_num)))
    elif choice == "3":
        print("Exiting...")
        break
    else:
        input("Wrong option. Press any key to continue...")