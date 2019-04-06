import random
import timeit
import math
######### 1.


def search_min_num_with_for():

    numlist = []
    maxmin = 1000
    for i in range(0, 10000):
        numlist.append(random.randint(-1000, maxmin))

    for j in numlist:
        if j < maxmin:
            maxmin = j
    return maxmin, numlist.index(maxmin)


statement = "search_min_num_with_for()"
setup = "from __main__ import search_min_num_with_for"
print(timeit.timeit(statement, setup=setup, number=100))


def search_min_num_with_while():

    numlist_2 = []
    maxmin = 1000
    i = 10000
    while i > 0:
        numlist_2.append(random.randint(-1000, maxmin))
        i -= 1
    j = 0
    while j < len(numlist_2):
        if numlist_2[j] < maxmin:
            maxmin = numlist_2[j]
        j += 1

    return maxmin, numlist_2.index(maxmin)

statement_2 = "search_min_num_with_while()"
setup_2 = "from __main__ import search_min_num_with_while"
print(timeit.timeit(statement_2, setup=setup_2, number=100))

##### Первая реализация через "for" работает примерно на 13% быстрее, чем через цикл "while"

########### 2.

# First brute force algorithm searching for i-prime number without Sieve of Eratosthenes

# Function isqrt(n) will find largest divisor for number "n"


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


# Function isprime(n) will check if integer is a prime number using brute force

def isprime(n):
    num_is_prime = True
    if n == 2:
        num_is_prime = True
    else:
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                num_is_prime = False
    return num_is_prime

# Function find_prime_num will create a list of prime numbers and break once it gets to the right one

def find_prime_num(i):
    prime_num_list = []
    for j in range(2, 1000000):
        if isprime(j):
            prime_num_list.append(j)
        if len(prime_num_list) == i:
            print(prime_num_list)
            break


statement_3 = "find_prime_num(1000)"
setup_3 = "from __main__ import find_prime_num"
print(timeit.timeit(statement_3, setup=setup_3, number=10))


# Function will use Sieve of Eratosthenes to find the i-prime number

def prime_sieve(i):
    sieve_num_list = []
    multiples_list = []
    for j in range(2, 10000):
        if j not in multiples_list:
            sieve_num_list.append(j)
            if len(sieve_num_list) == i:
                break
            for k in range(j * j, 100000, j):
                multiples_list.append(k)


statement_4 = "prime_sieve(1000)"
setup_4 = "from __main__ import prime_sieve"
print(timeit.timeit(statement_4, setup=setup_4, number=10))

# Нахождение простого числа с помощью Решето Эратосфена значительно увеличивает время поиска ~ в 100 раз :)
# 0,45 секунд против 58 секунд.
# Возможно это связано с неверной реализацией алгоритма в моем конкретном примере.
