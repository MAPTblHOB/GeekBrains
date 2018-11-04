print('Во втором массиве сохранить индексы четных элементов первого массива. \nИндексация начинается с нуля.\n')
from random import random
N = 10
arr = [0]*N
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print('Первый массив: ', arr)
print('Индексы четных элементов: ', even)
