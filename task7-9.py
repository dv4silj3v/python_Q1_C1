# 7.

n = int(input("n = "))

k = 1
num_sum = 0
while k <= n:
    num_sum += k
    k += 1

formula = n * (n + 1) / 2

if formula == num_sum:
    print("Correct!")
else:
    print("Incorrect!")

# 8.

repeats = []
n = int(input("n = "))
k = 0

while k < n:
    repeats.append(int(input("{} - e number: ".format(k + 1))))
    k += 1

search_number = int(input("Enter the digit: "))
count = repeats.count(search_number)

print("{} digits in a number".format(count))

# 9.

numstring = str(input("Please enter random numbers, dedicated by space: "))
numlist = numstring.split(" ")

max_sum = 0
digit_sum = 0

for i in numlist:
    for j in str(i):
        digit_sum += int(j)
    if digit_sum > max_sum:
        max_sum = digit_sum

print(max_sum)
