# task1 - Генератор Фибоначчи
def fibonacci():
    """
    Генератор, который генерирует последовательность Фибоначчи бесконечно,
    возвращая по одному числу за раз.
    """
    a, b = 0, 1
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
def unique_data_gen(data):
    """
    Генератор, который принимает список элементов и выдаёт только уникальные значения,
    сохраняя порядок их появления в исходном списке.
    """
    s = set()
    for item in data:
        if item not in s:
            s.add(item)
            yield item

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
for value in unique_data_gen(data):
    print(value)