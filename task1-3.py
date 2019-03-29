import random
# 1.
numlist = []

for i in range(9, 1000000):
    z = 0
    for j in range(2, 10):
        z = z + (i % j)
    if z == 0:
        numlist.append(i)
print(len(numlist))

# 2.
numlist = []
for i in range(0, 10):
    numlist.append(random.randint(1, 1000))
print(numlist)
even_num_index = []

for num in numlist:
    if num % 2 == 0:
        even_num_index.append(numlist.index(num))
print(even_num_index)

# 3.
maxnum = 0
minnum = 1000
for item in numlist:
    if item > maxnum:
        maxnum = item
    if item < minnum:
        minnum = item
numlist[numlist.index(minnum)], numlist[numlist.index(maxnum)] = numlist[numlist.index(maxnum)], numlist[numlist.index(minnum)]
print(numlist)
