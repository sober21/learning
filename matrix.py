#  задачи связанные с матрицей[список списков]


def square_matrix(num: int, char=0) -> list:
    '''создаёт квадратную матрицу размерами num x num. По умолчанию заполнено нулями(0)'''

    matrix = [[char] * num for _ in range(num)]
    return matrix


def regular_matrix(num1: int, num2: int, char=0) -> list:
    '''создаёт матрицу размерами num1 x num2 и заполняет символом(char(по умолчанию 0)) '''

    matrix = [[char] * num2 for _ in range(num1)]
    return matrix


def filling_in_the_matrix_by_columns(num1: int, num2: int) -> list:
    '''заполняет матрицу по столбам от 1 до num1 x num2'''
    matrix = regular_matrix(num1, num2, char=0)
    count = 0
    for i in range(num2):
        for j in range(num1):
            count += 1
            matrix[j][i] = str(count).ljust(3)
    return matrix


def area_matrix(matrix: list) -> str:
    matrix = [[int(j) for j in i] for i in matrix]
    mx = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(i + 1):
            if matrix[i][j] > mx:
                mx = matrix[i][j]
    return mx


def filling_the_matrix(num: int) -> list:
    '''заполняет главную и побочную диагональ единицами (1)'''

    matrix = square_matrix(num)
    for i in range(num):
        matrix[i][i] = 1
        matrix[i][num - i - 1] = 1
    return matrix


def filling_the_matrix_2(num: int) -> list:
    '''заполянет матрицу определённным образом: диагонали заполняются цифрой 1, так же как и пространство между
    диагоналями сверху и снизу. Остальное пространство заполняется нулями'''
    matrix = square_matrix(num)
    for i in range(n):
        for j in range(num):
            if i == j or num == j + i + 1 or (j > i and num > j + 1 + i) or (j < i and num < j + 1 + i):
                matrix[i][j] = 1
    return matrix


def filling_the_matrix_3(num1: int, num2: int) -> list[int]:
    '''заполняет матрицу определённым образом: первая строка от 1 до num2, вторая - от 2 до num2, 1,
    третья - от 3 до num2, 1, 2 и т.д.
    Например: num1 = 3, num2 = 4 -> [[1,2,3,4],[2,3,4,1],[3,4,1,2]]'''
    matrix = regular_matrix(num1, num2)
    if num1 <= num2:
        for i in range(num1):
            for j in range(num2):
                matrix[i][j-i] = j+1
    else:
        for i in range(num1):
            for j in range(num1):
                if num2 > j-i >= -num2:
                    if j+1 > num2:

                        matrix[i][j-i] = j+1 -num2
                    else:
                        matrix[i][j - i] = j + 1

    return matrix

def sum_row_matrix(matrix: list) -> str:
    '''проверяет, что квадрат магический, то есть он состоит из всех чисел(все числа разные) от 1 до n**2 и сумма
    его строк, столбцов и диагоналей одинакова'''

    flag = 'YES'
    my_list = []
    for i in range(len(matrix)):  # проверяем, что числа в нужном диапазоне и не повторяются
        for j in range(len(matrix)):
            if matrix[i][j] not in my_list and len(matrix) ** 2 >= matrix[i][j] > 0:
                my_list.append(matrix[i][j])
            else:
                flag = 'NO'
                return flag
    total = sum(matrix[0])
    for i in matrix:  # считаем сумму строк
        if total == sum(i):
            continue
        else:
            flag = 'NO'
            break
    sum_cols = 0
    for cols in range(len(matrix)):  # считаем сумму столбцов
        for row in range(len(matrix)):
            sum_cols += matrix[row][cols]
        if sum_cols == total:
            sum_cols = 0
        else:
            flag = 'NO'
            break
    main_diagonals = 0
    sec_diagonal = 0
    for i in range(len(matrix)):  # считаем сумму диагоналей
        main_diagonals += matrix[i][i]
        sec_diagonal += matrix[i][len(matrix) - 1 - i]
    if main_diagonals != total or sec_diagonal != total:
        flag = 'NO'

    return flag


def matr_chess(matrix: list, num: list):
    '''делает матрицу в виде шахматной доски, где вместо черных и белых клеток стоят точки(".") и звёздочки("*")'''
    for row in range(int(num[0])):
        if row % 2 == 0:
            for cols in range(0, int(num[1]), 2):
                matrix[row][cols] = '.'
        else:
            for cols in range(1, int(num[1]), 2):
                matrix[row][cols] = '.'
    for row in matrix:
        print(*row)


if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    for row in filling_the_matrix_3(n, m):
        print(*row)
