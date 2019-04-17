import random
from collections import deque
import itertools


a = [random.randint(0, 50) for z in range(50)]
print("Source array: {}".format(a))


def merge_sort(a):
    if len(a) <= 1:
        return a

    new_size = len(a) // 2

    left = deque(itertools.islice(a, 0, new_size))
    right = deque(itertools.islice(a, new_size, len(a)))

    left = merge_sort(left)
    right = merge_sort(right)

    for k in range(len(a)):
        if len(left) == 0:
            a[k] = right.popleft()
        elif len(right) == 0:
            a[k] = left.popleft()
        else:
            if left[0] <= right[0]:
                a[k] = left.popleft()
            else:
                a[k] = right.popleft()

    return a


print("Sorted array: {}".format(merge_sort(a)))