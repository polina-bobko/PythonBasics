num = float(input('Введите число: '))
print(f'Округленное вверх: {math.ceil(num)}')
print(f'Округленное вниз: {math.floor(num)}')

num = int(input("Введите число: "))
sum_result = 0
i = 1
while i <= num:
    sum_result += i
    i += 1
print("Сумма чисел от 1 до", num, "=", sum_result)

n = int(input('Enter a number: '))
sum_result = 0
while n >= 1:
    sum_result += n
    n -= 1
print(sum_result)

# num = int(input('Введите число: '))
# i = 0
# list=[]
# while i != num:
#     i += 1
#     list.append(i)
# print(sum(list))

import math
number = int(input("Введите число: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
factorial2 = math.factorial(number)
print("Факториал числа", number, "первым способом:", factorial)
print("Факториал числа", number, "вторым способом:", factorial2)
print("Результаты равны?", factorial == factorial2)

import math
num = int(input("Введите число: "))
res1 = math.factorial(num)
print('Факториал числа 5 первым способом:', res1)
res2 = 1
while num >= 1:
    res2 *= num
    num -= 1
print('Факториал числа 5 вторым способом:', res2)
print('Результаты равны?', res1 == res2)

sum = 0
while True:
    cost = float(input('Введите цену товара: '))
    if cost == 0:
        print('Сумма покупки:', round(sum))
        break
    sum += cost
a = int(input('Покупатель передал: '))
print('Сдача', round(a - sum), 'евро')

import math
total = 0
while True:
    price = float(input("Введите цену товара (0 для завершения): "))
    if price == 0:
    break
    total += price
# Округляем сумму покупки до целого числа
rounded_total = round(total)
# Рассчитываем сумму, которую передаёт покупатель
payment = math.ceil(rounded_total / 100) * 100
# Рассчитываем сдачу
change = payment - rounded_total
# Выводим результаты
print("Сумма покупки:", rounded_total, "евро")
print("Покупатель передал:", payment, "евро")
print("Сдача:", change, "евро")


sum = 0
sum_min = 0
while True:
    cost = int(input('Введите доход, расход или \'0\' для получения итога: '))
    if cost > 0:
        sum = sum + cost
    elif cost < 0:
        sum_min = sum_min - cost
    else:
        print('Доходы: ', sum)
        print('Расходы: ', sum_min)
        break
print('Итоговый баланс:' , sum - sum_min)

n = int(input("Сколько чисел Фибоначчи вывести? "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1

number = int(input("Введите число: "))
original_number = number
num_digits = 0
temp = number
# Подсчет количества цифр
while temp > 0:
    num_digits += 1
    temp //= 10
sum_of_powers = 0
temp = number
# Вычисление суммы цифр, возведенных в степень num_digits
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10
    if original_number == sum_of_powers:
        print("Число", original_number,"является числом Армстронга.")
    else:
        print("Число", original_number,"не является числом Армстронга.")

num = int(input("Введите число: "))
original = num
temp = num
n = 0
while temp > 0:
    temp //= 10
    n += 1
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
if sum == original:
    print("Число", original, "является числом Армстронга.")
else:
    print("Число", original, "не является числом Армстронга.")