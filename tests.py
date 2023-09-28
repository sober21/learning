from tasks2 import number_to_words


if __name__ == '__main__':
    assert number_to_words(99)== 'девяносто девять'
    assert number_to_words(3)== 'три'
    assert number_to_words(17)== 'семнадцать'
    assert number_to_words(50)== 'пятьдесят'
    assert number_to_words('')== "Введите целое число от 1 до 99"
    assert number_to_words('34')== "Введите целое число от 1 до 99"
    assert number_to_words('sd5')== "Введите целое число от 1 до 99"
    assert number_to_words('%%')== "Введите целое число от 1 до 99"
    assert number_to_words(100)== "Введите целое число от 1 до 99"
    assert number_to_words(0)== "Введите целое число от 1 до 99"
    assert number_to_words([1])== "Введите целое число от 1 до 99"
    assert number_to_words(-1)== "Введите целое число от 1 до 99"
    
