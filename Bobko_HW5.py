# Task 1 (min, max, mid)
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
max_num = num1
if max_num < num2:
    max_num = num2
if max_num < num3:
    max_num = num3

#or max_num=max(num1, num2, num3)

min_num = num1
if min_num > num2:
    min_num = num2
if min_num > num3:
    min_num = num3

#or min_num = min(num1, num2, num3)

if num1 != min_num and num1 != max_num:
    mid_num = num1
elif num2 != min_num and num2 != max_num:
    mid_num = num2
else:
    mid_num = num3

print('Числа в порядке возрастания:', min_num, mid_num, max_num)

# Task 1 (swap)
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num3, num2 = num2, num3
if num1 > num2:
    num1, num2 = num2, num1

#or
# if num1 > num2:
#     num1, num2 = num2, num1
# if num1 > num3:
#     num1, num3 = num3, num1
# if num2 > num3:
#     num2, num3 = num3, num2

print('Числа в порядке возрастания:', num1, num2, num3)

# Task 2
year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Год является високосным.', '\n---------------------------------------\n', sep='\n')
else:
    print('Год не является високосным.', '\n---------------------------------------\n', sep='\n')

# Task 2
year = int(input("Введите год: "))

if year % 400 == 0:
    print("Год является високосным.")
else:
    if year % 100 == 0:
        print("Год не является високосным.")
    else:
        if year % 4 == 0:
            print("Год является високосным.")
        else:
            print("Год не является високосным.")
