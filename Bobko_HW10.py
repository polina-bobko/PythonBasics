# Торговый автомат
total = int(input("Введите стоимость товара: "))
coins = [50, 10, 5, 2, 1]
for coin in coins:
        s = total // coin
        if s > 0:
            print("Внесите монеты номиналом", coin, ":", s)
            total -= s * coin

# total = int(input("Введите стоимость товара: "))
# coins = [50, 10, 5, 2, 1]
#
# for coin in coins:
#     count = 0
#     while total >= coin:
#         total -= coin
#         count += 1
#     if count > 0:
#         print("Внесите монеты номиналом", coin, ":", count)

# Квадрат нечетных чисел
nums = input("Введите числа без пробела: ")
digits = []
for ch in nums:
    digits.append(int(ch))
print("Изначальный список:", digits)
new_digits = list()
for digit in digits:
    if digit % 2 == 0:
        new_digits.append(digit)
    else:
        new_digits.append(digit**2)
print("Измененный список:", new_digits)

# numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
# new_numbers = []
# for n in numbers:
#     new_numbers.append(n if n % 2 == 0 else n**2)