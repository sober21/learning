# Будут приведены 3 цикла for, задача которых определить - является ли число простым(делится только на 1 и на себя)
# Для примера используется число: 1234567890

import time


def example1():
    # Тут перебираются все числа от 2 до num-1

    num = int(input())
    flag = True
    start = time.time()
    for i in range(2, num):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        print('Число простое')
    else:
        print('Число составное')
    end = time.time()
    return start - end


def example2():
    # Перебор чисел от 2 до num//2+1

    num = int(input())
    flag = True
    start = time.time()
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        print('Число простое')
    else:
        print('Число составное')
    end = time.time()
    return start - end


def example3():
    # Перебираются числа от 2 до (корня из num)+1

    num = int(input())
    flag = True
    start = time.time()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        print('Число простое')
    else:
        print('Число составное')
    end = time.time()
    return start - end


# В первом случае ушло более минуты
# Во втором - 30 секунд
# Третий пример показал результат 0,002 секунды
# Вот так при помощи правильных условий можно в несклько тысяч раз ускорить процесс.

if __name__ == '__main__':
    print(example3())
