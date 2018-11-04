print('Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. \nВведите "0" чтобы остановить ввод чисел.')
num = int(input('Введите число: '))
max_sum = 0
max_num = 0
while num != 0:
    temp_num = num
    temp_sum = 0
    while num > 0:
        temp_sum += num % 10
        num //= 10
    if temp_sum > max_sum:
        max_sum = temp_sum
        max_num = temp_num
    num = int(input('Введите число: '))
print('С максимальной суммой цифр', max_sum,  'число', max_num,' идет первым по счету из всех возможно введенных чисел с такой же суммой цифр ;o)')
