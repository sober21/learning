def area_matrix(matrix: list) -> str:
    matrix = [[int(j) for j in i] for i in matrix]
    mx = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(i + 1):
            if matrix[i][j] > mx:
                mx = matrix[i][j]
    return mx


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
    n = input().split()
    matr = [['*'] * int(n[1]) for _ in range(int(n[0]))]
    matr_chess(matr, n)
