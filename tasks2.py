# Тут просто решаю задачи

import math


def sum_minus():
    mx = -(pow(10, 6))
    s = 0
    for i in range(5):
        x = int(input())
        if x < 0:
            s += x

            if x > mx:
                mx = x
    if s == 0:
        print("NO")
    else:
        print(s)
        print(mx)


def max_de_3():
    n = abs(int(input()))
    max_digit = n % 10
    while n > 0:
        digit = n % 10
        if digit % 3 == 0:
            if digit > max_digit:
                max_digit = digit
        n = n // 10
    if max_digit >= 0 and max_digit % 3 == 0:
        print(max_digit)
    else:
        print("NO")


def sum_lists(m, l):
    '''выводит сумму чисел с одинаковыми индексами'''
    for i in range(len(m)):
        for j in range(len(l)):
            if i == j:
                print(int(m[i]) + int(l[j]), end=' ')


def draw_box(height, width):
    '''выводит пустотелый прямоугольник из звёздочек с высотой hiegth и шириной widht'''
    print('*' * width)
    print(*['*' + (width - 2) * ' ' + '*' for _ in range(height - 2)], sep='\n')
    print('*' * width)


def draw_triangle():
    '''выводит равнобедренный треугольник из звёздочек'''
    for i in range(1, 9):
        for j in range(1, 16):
            print(' ' * (8 - i), (15 - 2 * (8 - i)) * '*', sep='')
            break


def print_digit_sum(num):
    '''выводит сууму цирф числа num'''
    return sum([int(i) for i in str(num)])


def merge(list1, list2):
    '''соединяет 2 списка и сортирует их'''
    list1.extend(list2)
    list1.sort()
    return list1


def get_next_prime(num):
    '''выводит следующее простое число после num'''
    for i in range(1, num + 1):
        count = 0
        for j in range(1, num + i):
            if (num + i) % (j + 1) == 0:
                count += 1

        if count == 1:
            return num + i


def is_password_good(password):
    '''проверяет правильность пароля(не менее 8 символов, хотя бы 1 цифра, 1 строчная буква, 1 заглавная буква)'''

    if len(password) >= 8:
        dig = [i for i in password if i.isdigit()]
        low = [i for i in password if i.isalpha() if i.lower() == i]
        upp = [i for i in password if i.isalpha() if i.upper() == i]

        if len(dig) > 0 and len(low) > 0 and len(upp) > 0:
            return True
        else:
            return False
    else:
        return False


def is_valid_password_beegeek(password):
    '''проверяет правильность пароля для Beegeek(a:b:c, где a - число палиндром, b - простое число, c - чётное'''

    myl = password.split(':')
    if len(myl) != 3:
        return False
    prime = [i for i in range(2, int(myl[1])) if int(myl[1]) % i == 0]
    return myl[0] == myl[0][::-1] and len(prime) == 0 and int(myl[2]) % 2 == 0


def is_correct_bracket(text):
    '''проверяет, чтобы каждой открывающей скобочке нашлась закрывающая. Закрывающая скобка не может быть левее
    открывающей'''
    a = 0
    b = 0
    if len(text) % 2 != 0 or text.count('(') != text.count(')'):
        return False
    for i in text:
        if i == '(':
            a += 1
        elif i == ')':
            b += 1
        if b > a:
            return False

    return True


def convert_to_python_case(text):
    '''делает из CamelCase snake_case'''
    s = ''
    for i in text:
        s += i
        if i.upper() == i and i.isalpha():
            d = s[::-1].replace(i, i + '_', 1)
            s = d[::-1]
    return s[1:].lower()


def refutation_of_the_Euler_hypothesis():
    '''выводит числа опровергающие гипотезу Эйлера'''
    for e in range(150, 1, -1):
        for d in range(1, 151):
            for c in range(1, 151):
                for b in range(1, 151):
                    for a in range(1, 151):
                        if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                            print(a, b, c, d, e)


def number_to_words(num: int) -> str:
    '''переводит числа в русские слова и выводит'''
    numbers = ["нуль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    from_10_to_19 = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
                     "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    if not type(num) == int:
        return "Введите целое число от 1 до 99"
    if 0 < num < 10:
        for i in range(len(numbers)):
            if i == num:
                return numbers[i]
    elif 20 > num > 9:
        for i in range(len(from_10_to_19)):
            if i + 10 == num:
                return from_10_to_19[i]
    elif num % 10 == 0 and 0<num < 100:
        for i in range(len(tens)):
            if i == num // 10 - 2:
                return tens[i]
    elif 99 >= num > 20:
        for i in range(len(tens)):
            if i == num // 10 - 2:
                for j in range(len(numbers)):
                    if j == num % 10:
                        return tens[i] + ' ' + numbers[j]
    else:
        return "Введите целое число от 1 до 99"

def liststs(mylist):
    '''на вход подаётся список списков с числами'''
    ''' функция возвращает список нечетных по порядку списков с нечетными по порядку числами'''

    no_even_list = [mylist[i] for i in range(len(mylist)) if i % 2 == 0]
    main_list = []
    for i in no_even_list:
        if len(i) > 0:
            list1 = []
            for j in range(len(i)):
                if j % 2 == 0:
                    list1.append(i[j])
            main_list.append(list1)
    return main_list

def is_magic(date):
    '''на вход подаётся дата(12.12.1992). Возвращает True, если число умноженное на месяц равно последним 2 цифрам года'''
    d = date.split('.')
    return int(d[0])*int(d[1]) == int(d[2][2:])


def is_pangram(text):
    '''возрвращает True, если в text есть все буквы английского алфавита'''
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    count = 0
    for i in alphabet:
        if i in text.lower():
            count += 1
    return count == 26






if __name__ == '__main__':
    print(tuple('1', '2'))
