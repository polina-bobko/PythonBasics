# Число в конце
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_strings = []
for st in strings:
    for index in range(len(st)):
        if st[:index].isalpha() and st[index:].isdigit():
            new_strings.append(st)
            break

print("Строки с цифрами только в конце:", new_strings)

# ИЛИ - лучше для памяти, не забивается срезами
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# new_strings = []
# for st in strings:
#     i = 0
#     while i < len(st) and st[i].isalpha():
#         i += 1
#     if i > 0 and st[i:].isdigit():
#         new_strings.append(st)
# print("Строки с цифрами только в конце:", new_strings)

# Удаление кратных
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
n = int(input("Введите число для удаления кратных ему элементов: "))
new_numbers = []
for value in numbers:
    if value % n != 0:
        new_numbers.append(value)
print("Список без кратных значений:", new_numbers)

# Порядок четных
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
new_numbers = []
even_nums = []
for value in numbers:
    if value % 2 != 0:
        new_numbers.append(value)
    else:
        new_numbers.append(0)
        even_nums.append(value)
even_nums.sort()
for index, value in enumerate(new_numbers):
    if value == 0:
        new_numbers[index] = even_nums.pop()
print("Список после сортировки:", new_numbers)

# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# even_nums = sorted([n for n in numbers if n % 2 == 0], reverse=True)
# result = []
# even_index = 0
# for n in numbers:
#     if n % 2 == 0:
#         result.append(even_nums[even_index])
#         even_index += 1
#     else:
#         result.append(n)
# print("Список после сортировки:", result)