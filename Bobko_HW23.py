# task1 - Объединение данных в строку
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

def join_data(data: list) -> str:
    """
    Преобразует список любых данных в строку, объединяя элементы через ' | '.

    :param data: Список элементов любого типа (числа, строки, списки, словари)
    :return: Строка с объединёнными элементами
    """
    return " | ".join([str(item) for item in data])


print(join_data(data))

# task2 - Сумма вложенных чисел
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

from functools import reduce

def get_total_score(data: list[dict[str, list[int]]]) -> int:
    """
    Считает сумму всех чисел во вложенных списках словарей.

    :param data: Список словарей, где каждый словарь содержит имя пользователя и список баллов "scores"
    :return: Общая сумма всех чисел
    """
    return reduce(
        lambda acc, user: acc + sum(user["scores"]),
        data,
        0
    )

print("Итоговый балл:", get_total_score(data))
