# Задачи связанные с матрицей(списком списков)

def square_matrix(num: int) -> list:
    '''создаёт квадратную матрицу размерами num x num. По умолчанию заполнено None'''

    matrix = [[None] * num for _ in range(num)]
    return matrix


def regular_matrix(num1: int, num2: int, char=0) -> list:
    '''создаёт матрицу размерами num1 x num2 и заполняет символом(char(по умолчанию 0)) '''

    matrix = [[char] * num2 for _ in range(num1)]
    return matrix


def sum_matrix(matrix_1: list, matrix_2: list) -> list:
    result = regular_matrix(n, m)
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]
    return result


def multiplication_matrix(matrix_1: list, matrix_2: list) -> list:
    result = regular_matrix(n,k)
    for i in range(n):
        sum = 0
        for j in range(k):
            for h in range(m):
                sum += matrix_1[i][h]*matrix_2[h][j]
            result[i][j] = sum

    return result


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
    m1 = [[int(i) for i in input().split()] for _ in range(n)]
    spase = input()
    m,k = [int(i) for i in input().split()]
    m2 = [[int(i) for i in input().split()] for _ in range(m)]
    for row in multiplication_matrix(m1, m2):
        print(*row)
