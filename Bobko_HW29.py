# task1 - Генератор Фибоначчи
from typing import Generator

def fibonacci(a: int=0, b: int=1) -> Generator[int]:
    """
    Генератор, который генерирует последовательность Фибоначчи бесконечно,
    возвращая по одному числу за раз.
    По умолчанию начинается с 0 и 1.
    :param a: Принимает число(int), по умолчанию 0.
    :param b: Принимает число(int), по умолчанию 1.
    :return: Выводит генератор, генерирующий последовательность Фибоначчи бесконечно.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Аргументы a и b должны быть целыми числами.')
    if a < 0 or b < 0:
        raise ValueError('Числа Фибоначчи не могут быть отрицательными.')
    if b < a:
        raise ValueError('Второе число(b) должно быть больше или равно первому(a).')
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
while True:
    value = next(fib)
    if value > 50:
        break
    print(value)

# task2 - Генератор уникальных элементов
from typing import Iterable, Iterator


def unique_data_gen(data: Iterable) -> Iterator:
    """
    Генератор, который принимает список элементов и выдаёт только уникальные значения,
    сохраняя порядок их появления в исходном списке.

    :param data: Принимает итерируемый объект (например, list).
    :return: Возвращает генератор с уникальными значениями.
    """
    if not isinstance(data, Iterable):
        raise TypeError("data должен быть итерируемым объектом (Iterable).")

    seen = set()

    for item in data:
        if item not in seen:
            seen.add(item)
            yield item


data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

for value in unique_data_gen(data):
    print(value)