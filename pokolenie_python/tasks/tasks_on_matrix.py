# Задачи связанные с матрицей(списком списков)

def square_matrix(num: int) -> list:
    '''создаёт квадратную матрицу размерами num x num. По умолчанию заполнено None'''

    matrix = [[None] * num for _ in range(num)]
    return matrix


def regular_matrix(num1: int, num2: int, char: int | str) -> list:
    '''создаёт матрицу размерами num1 x num2 и заполняет символом(char) '''

    matrix = [[char] * num2 for _ in range(num1)]
    return matrix


def side_diagonal_0_and_2():
    '''заполняет матрицу по принципу: побочная диагональ заполняется цифрой 1, пространство выше побочки - 0,
    ниже - 2'''

    pass


def filling_the_matrix_in_order(num1: int, num2: int) -> list:
    '''заполняет матрицу размером num1 x num2 числами по порядку от 1 до num1*num2'''

    matrix = regular_matrix(num1, num2, 0)
    count = 0
    for i in range(num1):
        for j in range(num2):
            count += 1
            matrix[i][j] = str(count).ljust(3)

    return matrix


if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    for row in filling_the_matrix_in_order(n, m):
        print(*row)
