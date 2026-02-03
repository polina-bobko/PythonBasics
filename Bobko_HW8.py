# Task 1 - Проверка кодировки

sym = input("Введите символ: ")
print("Код Unicode:", ord(sym))
if 0 <= ord(sym) <= 127:
    print("ASCII символ: True")
else:
    print("ASCII символ: False")

# print("ASCII символ:", sym.isascii())

# Task 2 - Подстрока с заполнением

s = input("Введите строку: ")
start = int(input("Введите начальный индекс: "))
end = int(input("Введите конечный индекс: "))

if start < 0 or end < 0 or start >= end:
    print("Введите значения больше или равно 0 и start < end")
else:
    substring = s[start:end]
    if end > len(s):
        substring += '_' * (end - len(s))
    print("Подстрока:", substring)

#sub = s[start:end]
#print("Подстрока:", sub + '_' * max(0, end - len(s)))

# Task 3 - Подсчёт символа

string = input("Введите строку: ")
symbol = input("Введите символ: ")
i = 0
n = 0
while i < len(string):
    if string[i] == symbol:
        n += 1
    i += 1
print("Символ", symbol, "встречается", n, "раз(а).")

#print("Символ", symbol, "встречается", string.count(symbol), "раз(а).")

# Task 4 - Инвертирование строки без цифр

w = input("Введите строку: ")
reversed_w = w[::-1]
i = 0
new_w = ''

while len(w) > i:
    if reversed_w[i].isdigit():
        i += 1
        continue
    else:
        new_w += reversed_w[i]
        i += 1

print("Результат:",new_w)

#or
# w = input("Введите строку: ")
# i = len(w) - 1
# new_w = ""
#
# while i >= 0:
#     if not w[i].isdigit():
#         new_w += w[i]
#     i -= 1
#
# print("Результат:", new_w)