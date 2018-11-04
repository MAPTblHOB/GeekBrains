print('В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. Индексация начинается с 1.')
from random import random
N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

mn = 0
mx = 0

for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print('Минимальный элемент массива - %d стоит на позиции - %d, а максимальный элемент - %d - на позиции - %d.' % (arr[mn], mn+1, arr[mx], mx+1))
print('Меняем их местами')
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b

for i in range(15):
    print(arr[i], end = ' ')
print()
