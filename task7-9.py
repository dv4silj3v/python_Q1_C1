import random
# 7.
numlist = [1, 3, -4, 5, -8, -49, 4, 343, 23, 234, 6, 764, -234]
minnum_1 = 1000
minnum_2 = 1000

for num in numlist:
    if num < minnum_1:
        minnum_1 = num
numlist.remove(minnum_1)
for num in numlist:
    if num < minnum_2:
        minnum_2 = num
print(minnum_1, minnum_2)

# 8.

n = 4   # matrix size

# Filling table with random elements instead of hand input
elements = random.sample(range(100), n * n)
print(elements)

matrix = [elements[index:index + n] for index in [n * i for i in range(n)]]

# Adding last element in each row as a sum of elements in that row
for row in matrix:
    row_sum = 0
    for elem in row:
        row_sum = row_sum + elem
    row.append(row_sum)

for line in matrix:
    print(line)

# 9.
# Let's transposition matrix to work with rows
trans_matrix = list(map(list, zip(*matrix)))
minnum_column_list = []
maxnum_of_minnum = 0
for row in trans_matrix:
    minnum_column = 100000
    for elem in row:
        if elem < minnum_column:
            minnum_column = elem
    minnum_column_list.append(minnum_column)
print(minnum_column_list)
for item in minnum_column_list:
    if item > maxnum_of_minnum:
        maxnum_of_minnum = item
print(maxnum_of_minnum)