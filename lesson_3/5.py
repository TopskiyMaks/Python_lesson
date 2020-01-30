# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран
# его значение и позицию в массиве.

from random import random

N = 15
arr = [int(random()*100) for i in range(N)]
print(arr)

k = 0
index = -1
while k < N:
    if arr[k] < 0 and index == -1:
        index = k
    elif 0 > arr[k] > arr[index]:
        index = k
    k += 1

print(index + 1, ':', arr[index])

