print('Найти максимальный элемент среди минимальных элементов столбцов матрицы.\n')
print('1) Генерируем матрицу 10х10 с максимумом в 200\n')
from random import random
M = 10
N = 10
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*200)
        b.append(n)
        print('%4d' % n,end='')
    a.append(b)
    print()
print('\n2) Разбираем\n')
mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
    print('В столбце', j, 'минимальное значение', mn)
print('\n3) Итого: максимальное значение среди минимальных -', mx)
