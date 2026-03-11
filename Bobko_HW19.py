# task 1 Реверс словаря
data = {"a": 1, "b": 2, "c": 1, "d": 3}
# Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
reversed_data = {}
for key, value in data.items():
    if value not in reversed_data:
        reversed_data[value] = [key]
    else:
        reversed_data[value].append(key)
print("Перевернутый словарь:", reversed_data)

# task 2 Счётчик букв в словах
words = ["anna", "bennet", "john"]
# {'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}
d = {word: {letter:word.count(letter) for letter in set(word)} for word in words}
print(d)

# task 3 Распределение студентов по группам
# "Отличники": баллы >= 85
# "Хорошисты": баллы от 70 до 84
# "Троечники": баллы от 50 до 69
# "Не сдали": баллы < 50
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
grouped_students = {group: {} for group in groups}
for student, score in students.items():
    if score < 50:
        grouped_students["Не сдали"][student] = score
    elif score < 70:
        grouped_students["Троечники"][student] = score
    elif score < 85:
        grouped_students["Хорошисты"][student] = score
    else:
        grouped_students["Отличники"][student] = score
print(grouped_students)