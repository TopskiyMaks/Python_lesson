# 3. В массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.
from random import random

arr = [int(random()*100) for i in range(10)]
MIN = 0
MAX = 1
print(arr)

for i in range(len(arr)):
    if arr[i] < arr[MIN]:
        MIN = i
    elif arr[i] > arr[MAX]:
        MAX = i

b = arr[MIN]
arr[MIN] = arr[MAX]
arr[MAX] = b
print(arr)
