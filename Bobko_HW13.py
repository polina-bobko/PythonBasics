# Прогрессия увеличения
numbers = (3, 7, 2, 8, 5, 10, 1)
progression_list = [numbers[0]]
current_max = numbers[0]
for number in numbers[1:]:
    if number > current_max:
        progression_list.append(number)
        current_max = number
progression_tuple = tuple(progression_list)

print("Кортеж по возрастанию:", progression_tuple)

# Повторяющиеся элементы
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
dubbed_list = []
for number in numbers:
    if numbers.count(number) > 1 and number not in dubbed_list:
        dubbed_list.append(number)
dubbed_nums = tuple(dubbed_list)
for n in dubbed_nums:
    index_list = []
    for index, number in enumerate(numbers):
        if number == n:
            index_list.append(index)
    print(f"Индексы элемента {n}:", *index_list)