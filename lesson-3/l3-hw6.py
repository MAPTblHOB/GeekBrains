print('В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. \nСами минимальный и максимальный элементы в сумму не включать.\n')
print('Сгенерированный массив: \n')
from random import random
N = 10
a = [0] * N
for i in range(N):
    a[i] = int(random() * 50)
    print('%3d' % a[i], end = '')
print('\n')

min_id = 0
max_id = 0
for i in range(1, N):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print('Минимальный элемент - "',a[min_id], '".', 'Максимальный элемент - "', a[max_id],'".')

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
print('Между ними находятся элементы: ')
for i in range(min_id+1, max_id):
    summa += a[i]
    if summa != 0:
        print('%3d' % a[i], end = '')
print('\nСумма которых равна: ',summa)
