


def task_iosif_flavi(num1: int, num2: int) -> list:
    ''''''
    a_list = list(range(1, num1 + 1)) * 60

    while True:
        cur_list = []
        post_list = []
        for i in range(1, num1 + 1):
            if i < num2:
                cur_list.append(a_list[i - 1])
            elif i == num2:
                cur_del = a_list.pop(i - 1)

                while cur_del in cur_list:
                    cur_list.pop(cur_list.index(cur_del))

                post_list = a_list[i - 1:]
                while cur_del in post_list:
                    post_list.pop(post_list.index(cur_del))
                break

        a_list = post_list + cur_list
        if a_list.count(a_list[0]) == len((a_list)):
            return a_list[0]


    return a_list[0]


def rock_paper_scissors():
    '''камень, ножницы, бумага'''

    options = ["камень", "ножницы", "бумага"]
    results = ["ничья", "первый игрок", "второй игрок"]

    player_1_move = input()
    player_2_move = input()

    case = options.index(player_1_move) - options.index(player_2_move)
    res = results[case]

    return res


def play():
    t = input()
    r = input()
    if t == r:
        print("ничья")
    elif (t == "камень" and r == "ножницы" or r == "ящерица") or \
            (t == "ножницы" and r == "бумага" or r == "ящерица") or \
            (t == "бумага" and r == "камень" or r == "Спок") or\
            (t == "ящерица" and r == "Спок" or r == "бумага") or \
            (t == "Спок" and r == "ножницы" or r == "камень"):
        print("Тимур")
    else:
        print("Руслан")

def fff(a,b,c):
    if (a == 1 and b ==2 or c ==3) or (a ==2 and b == 3 or c ==1):
        print('yes')
    else:
        print('no')

def simple_task(a_list: list) -> list:
    a_list.insert(0, a_list.pop())
    return a_list


if __name__ == '__main__':
    simple_task([1,2,3])


