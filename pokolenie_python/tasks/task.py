def task_iosif_flavi(num1: int, num2: int) -> list:
    a_list = list(range(1, num1 + 1))*2

    while len(a_list) > 1:
        cur_list = []
        post_list = []
        for i in range(1, num1 + 1):
            if i < num2:
                cur_list.append(a_list[i-1])
            elif i == num2:
                cur_del = a_list.pop(i - 1)
                while cur_del in cur_list:
                    cur_list.pop(cur_list.index(cur_del))

                post_list = a_list[i-1:]
                while cur_del in post_list:
                    post_list.pop(post_list.index(cur_del))
                break


        a_list = post_list + cur_list

        if len(a_list) < num2:
            d = 0
            while len(a_list) != num2:
                if a_list[0] != a_list[-1]:
                    a_list.append(a_list[d])
                else:
                    a_list.append(a_list[d+1])
                d += 1
        # for i in range(num2, num1 + 1, num2):
        #     a_list.pop(i - 1)

    return a_list


if __name__ == '__main__':
    n, k = int(input()), int(input())
    print(task_iosif_flavi(n, k))
