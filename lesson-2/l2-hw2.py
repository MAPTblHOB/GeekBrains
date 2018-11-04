n = int(input('Посчитать четные и нечетные цифры введенного натурального числа: '))
even=odd=0
while n>0:
    if n%2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print("четных - %d, нечетных - %d" % (even, odd))
