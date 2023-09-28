def list_work_dublikate(s:str)->list:
    result = []
    letter = s[0]
    for i in s.split():
        if i == letter:
            result.append([])

        result.append(list(i))
    return result

if __name__ == '__main__':
    n = int(input())
    seq = [(input().split())for _ in range(n)]
    print(seq)