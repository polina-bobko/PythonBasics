# Task 1
# Таблица умножения
n = int(input("Введите число: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        value = i * j
        if value < 10:
            print("  ", value, end="")
        elif value < 100:
            print(" ", value, end="")
        else:
            print(value, end="")
    print()

# Task 2
# Лестница чисел

num = int(input("Введите число: "))
s = ''
for i in range(1, num + 1):
    if i == 1:
        s += str(i)
    else:
        s += " " + str(i)
    print(s)
    #print(s[:-1])

# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         if j == i:
#             print(j, end="")
#         else:
#             print(j, end=" ")
#     print()

# Task 3
# Удаление всех повторяющихся символов
text = input("Введите строку: ")
new_s = ''
for char in text:
    if char in new_s:
        continue
    new_s += char

print("Результат: ", new_s)

