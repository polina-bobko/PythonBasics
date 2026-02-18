# Прогрессия увеличения
numbers = (3, 7, 2, 8, 5, 10, 1)
progression_tuple = (numbers[0],)
current_max = numbers[0]
for index, number in enumerate(numbers[1:], start=1):
    if number > current_max:
        progression_tuple += (number,)
        current_max = number
print("Кортеж по возрастанию:", progression_tuple)

# Повторяющиеся элементы
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
dubbed_nums = tuple()
for number in numbers:
    if numbers.count(number) > 1 and number not in dubbed_nums:
        dubbed_nums += (number,)
indexes = tuple()
for n in dubbed_nums:
    for index, number in enumerate(numbers):
        if number == n:
            indexes += (index,)
    print(f"Индексы элемента {n}:", *indexes)
    indexes = tuple()