import random

a = [random.randint(-100, 100) for z in range(100)]
print("Source array: {}".format(a))


def bubble_sort(a):
    flag = True
    for n in range(1, len(a)):
        if not flag:
            break

        flag = False
        for i in range(len(a) - n):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True


bubble_sort(a)
print("Sorted array: {}".format(a))