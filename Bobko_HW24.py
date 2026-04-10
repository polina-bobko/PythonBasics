# task 1 - Сумма цифр числа
num = 43197

def get_sum(data: int) -> int:
    """
    Считает рекурсивно сумму всех цифр в числе.

    :param data: Целое число.
    :return: Целое число - сумма всех цифр.
    """
    if data < 10:
        return data
    else:
        last_digit = data % 10
        data = data // 10
        return last_digit + get_sum(data)

print(get_sum(num))

# task 2 - Сумма вложенных чисел
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

def get_nested_sum(data: list) -> int:
    '''
    Рекурсивно суммирует все числа во вложенных списках.

    :param data: Вложенный список, который может содержать: целые числа (int)
                 и другие списки (list), любой глубины вложенности
    :return: Целое число - сумма всех чисел во всех уровнях вложенности списка
    '''
    total = 0
    for item in data:
        if isinstance(item, list):
            total += get_nested_sum(item)
        else:
            total += item
    return total

print(get_nested_sum(nested_numbers))