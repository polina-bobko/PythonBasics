# Не уникальные числа
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
num_set = {n for n in set(numbers) if numbers.count(n)>1}
print("Числа, встречающиеся более одного раза:", sorted(num_set, reverse=True))

# Проверка подмножества
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

is_subset = True

for key, value in dict1.items():
    if key not in dict2 or dict2[key] != value:
        is_subset = False
        break
if is_subset:
    print("dict1 is a subset of dict2")
else:
    print("dict1 is not a subset of dict2")

# OR
# if dict1.items() <= dict2.items():
#     print("dict1 is a subset of dict2")
# else:
#     print("dict1 is not a subset of dict2")