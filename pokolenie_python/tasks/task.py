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


if __name__ == '__main__':

    assert task_iosif_flavi(2,1) == 2
    assert task_iosif_flavi(7,5) == 6
    assert task_iosif_flavi(50,25) == 5
    assert task_iosif_flavi(100,99) == 88


