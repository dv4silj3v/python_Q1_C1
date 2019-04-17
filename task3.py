import random

m = 7

arr_len = 2 * m + 1

arr = [random.randint(0, 100) for z in range(arr_len)]

print("Source array: {}".format(arr))


def med(arr):
    for i in range(len(arr)):
        left = 0
        right = 0

        for j in range(len(arr)):
            if i == j or arr[j] == arr[i]:
                continue
            elif arr[j] < arr[i]:
                left += 1
            elif arr[j] > arr[i]:
                right += 1
            else:
                raise Exception("Exiting..")

        med_len = (len(arr) - 1) / 2

        if left <= med_len and right <= med_len:
            return i


med_i = med(arr)
print("Median is {}, element with index {}".format(arr[med_i], med_i))