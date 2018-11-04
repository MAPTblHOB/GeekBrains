print('Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк, \nкуда автоматически вписывается сумма введенных элементов строки.')
M = 5
N = 4
last_elem = []
for i in range(N):
    temp_last_elem = []
    summ = 0
    i = i + 1
    print("%d-я строка:" % i)
    for j in range(M - 1):
        num = int(input())
        summ += num
        temp_last_elem.append(num)
    temp_last_elem.append(summ)
    last_elem.append(temp_last_elem)
 
for i in last_elem:
    print(i)
