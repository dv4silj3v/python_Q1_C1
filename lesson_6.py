import memory_profiler
import sys

### Для анализа памяти была использована первая задача пятого домашнего задания.
### В программе используется функция, которая генерирует выручку предприятия по кварталам, а также
### берет произвольное имя из подключаемого из файла UNIX словаря.
###
### В первой реализации чтение из файла с 99171 строкой создается в стандартный список words (list) с соответсвующим
### количеством элементов. Для 64bit ОС и python 3.7 подсчитаем примерное значение такого списка:
###  При средней длине строки в этом файле в 8 символов, размер одной строки с учетом переноса равен 37 + 8 + 2 = 47 байт.
###  Размер 99171 строки из этого файла будет равен: 99171 * 47 = 4661037 байт, плюс сам список, который
###  будет хранить на них ссылки: 40 + 8 * 99171 = 793408 байт.
###  Общяя память необходимая для хранение этого списка будет равна: 5454445 байт, или 5.2 Mb. Это значение близко
###  к значению прироста (increment), которое получено с помощью memory_profiler:
# Filename: /home/dmitry/PycharmProjects/Q1_C1/python_Q1_C1/lesson_6.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     14     15.8 MiB     15.8 MiB   @memory_profiler.profile()
#     15                             def company_generator(n):
#     16                                 """
#     17                                 This function will generate a list of companies with revenue by quarter.
#     18                                 :param n: number of companies to generate
#     19                                 :return: defaultdict
#     20                                 """
#     21
#     22     15.8 MiB      0.0 MiB       company_report = defaultdict(lambda: [0, 0, 0, 0])
#     23
#     24                                 # We are going to use "/usr/share/dict/words" file for Company Name Generator
#     25     15.8 MiB      0.0 MiB       with open('/usr/share/dict/words', 'r', encoding='UTF-8') as f:
#     26     22.7 MiB      6.9 MiB           words = f.readlines()
#     27     22.7 MiB      0.0 MiB       print(sys.getsizeof(words))
#     28     29.2 MiB      0.3 MiB       words = [x.strip() for x in words]
#     29
#     30                                 # Generate revenue for each company and each quarter
#     31     23.4 MiB      0.0 MiB       while n > 0:
#     32     23.4 MiB      0.0 MiB           company_name = random.choice(words)
#     33     23.4 MiB      0.0 MiB           company_report[company_name] = [random.randrange(10000, 100000), random.randrange(10000, 100000),
#     34     23.4 MiB      0.0 MiB                                           random.randrange(10000, 100000), random.randrange(10000, 100000)]
#     35     23.4 MiB      0.0 MiB           n -= 1
#     36
#     37     23.4 MiB      0.0 MiB       return company_report

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
    print(sys.getsizeof(words))
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
