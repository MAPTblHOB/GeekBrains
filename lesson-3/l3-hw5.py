print('В массиве найти максимальный отрицательный элемент. Индексация начинается с 1.')
from random import random
N = 10
arr = []
for i in range(N):
        arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
        if arr[i] < 0 and index == -1:
                index = i
        elif arr[i] < 0 and arr[i] > arr[index]:
                index = i
        i += 1

if index + 1 == 0:
    print('Максимальный отрицательный элемент в массиве отсутствует')
else:
    print('Максимальный отрицательный элемент массива "',arr[index],'" находится в позиции "', index+1,'"')
