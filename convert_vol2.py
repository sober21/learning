def convert_vol_2(a_list: list) -> list:
    match a_list:
        case []:
            return a_list
        case list():
            result = []
            current_list = []
            for i in a_list:
                match i:
                    case current_symbol if not current_list:
                        current_list.append(current_symbol)
                        sequence = current_symbol

                    case current_symbol if current_symbol in current_list:
                        current_list.append(current_symbol)
                        count = [current_symbol, current_list.count(current_symbol)]
                        sequence = tuple(count)

                    case current_symbol:
                        result.append(sequence)
                        current_list = []
                        current_list.append(current_symbol)
                        sequence = current_symbol
    match current_list:
        case [symbol]:
            result.append(symbol)
        case _:
            result.append(sequence)
    return result


if __name__ == '__main__':
    print(convert_vol_2(['a', 'a', 'h', 'e','e','e','l']))
