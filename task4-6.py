# 4.
numlist = [2, 7, -56, 45, -23, 5, 7, -2, -6, -45, 2, -345, 2, 7, 5, 5, 5, 5]
maxelem = 0
z = 0
x = 0

for i in numlist:
    z = numlist.count(i)
    if z > maxelem:
        maxelem = z
        x = numlist.index(i)
print(numlist[x])

# 5.
maxmin = 1000
for j in numlist:
    if j < maxmin:
        maxmin = j
print(maxmin, numlist.index(maxmin))

# 6.
minnum = 1000
maxnum = -1000
sumnum = 0
for elem in numlist:
    if elem > maxnum:
        maxnum = elem
    if elem < minnum:
        minnum = elem
print(minnum, maxnum)

if numlist.index(minnum) > numlist.index(maxnum):
    for i in range(numlist.index(maxnum) + 1, numlist.index(minnum) - 1):
        sumnum = sumnum + numlist[i]
if numlist.index(maxnum) > numlist.index(minnum):
    for i in range(numlist.index(minnum) + 1, numlist.index(maxnum) - 1):
        sumnum = sumnum + numlist[i]
if numlist.index(maxnum) == numlist.index(minnum):
    sumnum = maxnum
print(sumnum)


