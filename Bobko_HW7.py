# Task 1
# Напишите программу, которая вычисляет сумму цифр введённого числа.
sum = 0
num = int(input("Enter a number: "))
while num != 0:
    digit = num % 10
    sum += digit
    num //= 10

print("Sum =", sum)

# Task 2
# Напишите программу, которая запрашивает у пользователя целое число и определяет, является ли оно палиндромом.
# Число является палиндромом, если оно читается одинаково слева направо и справа налево.

# p = int(input("Введите целое число: "))
# if p < 0 or (p % 10 == 0 and p != 0):
#     print("Число не является палиндромом")
# else:
#     reversed_half = 0
#
#     while p > reversed_half:
#         reversed_half = reversed_half * 10 + p % 10
#         p //= 10
#
#     if p == reversed_half or p == reversed_half // 10:
#         print("Число является палиндромом")
#     else:
#         print("Число не является палиндромом")

p = int(input("Введите целое число: "))
if p < 0 or (p % 10 == 0 and p != 0):
    print("Число не является палиндромом")
else:
    original_num = p
    reversed_num = 0
    while p > 0:
        digit = p % 10
        reversed_num = reversed_num * 10 + digit
        p = p // 10

    if original_num == reversed_num:
        print(f"Число {original_num} является палиндромом.")
    else:
        print(f"Число {original_num} не является палиндромом.")

# Task 3

import random

target_number = random.randint(1, 100)
attempts_left = 10

print("Угадайте число от 1 до 100. У вас 10 попыток.")

attempts = 0

while attempts_left > 0:
    guess = int(input(f"Ваше предположение: "))
    attempts += 1
    attempts_left -= 1

    if guess < target_number:
        print("Загаданное число больше вашего.")
    elif guess > target_number:
        print("Загаданное число меньше вашего.")
    else:
        print(f"Поздравляем! Вы угадали число: {target_number}.")
        break

if guess == target_number:
    if attempts == 1:
        print("Отличная интуиция! Вы угадали с первой попытки!")
    elif attempts <= 3:
        print(f"Вы угадали число за {attempts} попытки. Отличный результат!")
    elif attempts <= 6:
        print(f"Вы угадали число за {attempts} попыток. Хороший результат!")
    else:
        print(f"Вы угадали число за {attempts} попыток. Нужно тренировать интуицию!")
else:
    print(f"К сожалению, вы не угадали. Загаданное число было: {target_number}.")