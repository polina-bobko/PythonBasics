# task 1 Простое число
def is_simple(num):
    if num <= 1:
        return "Error. Enter a positive integer greater than 1"
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


print(is_simple(0))
print(is_simple(12))
print(is_simple(13))

# task 2 Фильтрация чисел по чётности
def filter_numbers(filter_type: str, *args: int):
    s = []
    if filter_type == "even":
        for num in args:
            if num % 2 == 0:
                s.append(num)
    elif filter_type == "odd":
        for num in args:
            if num % 2 != 0:
                s.append(num)
    else:
        return "Incorrect filter type"
    return s

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

# task 3 Объединение словарей
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}


def merge_dicts(*args):
    d = {}
    for di in args:
        for key, value in di.items():
            d[key] = value
    return d

print(merge_dicts(dict1, dict2, dict3))

# opt 1 def merge_dicts(*args):
#       return {k: v for d in dicts for k, v in d.items()}
# opt 2 def merge_dicts(*args):
#     result = {}
#     for di in args:
#         result |= di  # объединяем словарь
#     return result
# opt 3 def merge_dicts(*dicts):
#     result = {}
#     for dct in dicts:
#         result.update(dct)
#     return result
