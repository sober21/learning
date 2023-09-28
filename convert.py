

def convert(a_list: list, symbol) -> list:
    if a_list:
        result = []
        current_symbol = a_list[0]
        current_list = []
        count = 1
        for char in a_list[1:]:
            match symbol:
                case current_symbol:
                    count += 1
                    current_symbol = char
                case _:
                    if count > 1:
                        current_list.append(current_symbol)
                        current_list.append(count)
                        result.append(tuple(current_list))
                        current_symbol = char
                        count = 1
                        current_list = []
                    else:
                        result.append(current_symbol)
                        current_symbol = char
                        count = 1
        if count > 1:
            current_list.append(current_symbol)
            current_list.append(count)
            result.append(tuple(current_list))
        else:
            result.append(current_symbol)
        return result
    else:
        return a_list

if __name__ == '__main__':
    print(convert([1,2,3,4,5,4,3,2,3,4,5,6,6,7,8,7,6,5,4,4,3]))
    assert convert([]) == []
