# Task 1
import math

x = float(input("Введите вещественное число: "))

result = math.floor(x + 0.5) if x >= 0 else math.ceil(x - 0.5)

# if x >= 0:
#     result = int(x + 0.5)
# else:
#     result = int(x - 0.5)

print("Округленное значение:", result)

# Task 2
a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

if a <= 0 or b <= 0:
    print("Ошибка: длины катетов должны быть положительными числами")
else:
    c = math.sqrt(a**2 + b**2)
    print("Длина гипотенузы:", c)
