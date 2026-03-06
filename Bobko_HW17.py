# Проверка на подмножество
set1 = {1, 2, 3, 4}
set2 = {2, 3}

is_subset = True

for item in set2:
    if item not in set1:
        is_subset = False
        break
print(is_subset)

#print("Содержит ли первое множество все элементы второго множества:", set1>=set2)
#print("Содержит ли первое множество все элементы второго множества:", set2<=set1)
#print("Содержит ли первое множество все элементы второго множества:", set2.issubset(set1))
#print("Содержит ли первое множество все элементы второго множества:", set1.issuperset(set2))

# Зеркальное подмножество
set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

if set1 >= set2:
    print("Подмножество: True")
    print("Разница:", set1 - set2)
elif set2 >= set1:
    print("Подмножество: True")
    print("Разница:", set2 - set1)
else:
    print("Подмножество: False")