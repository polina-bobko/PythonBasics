#Задание №1

print("Привет!")
name, age, color = input('Введите ваше имя: '), input('Введите ваш возраст: '), input('Введите ваш любимый цвет: ')
print("Привет, меня зовут " + name + ", мне " + age + " лет и мой любимый цвет " + color +"!")

#Задание 2

print("Она сказала: \"Привет!\"")
print('Она сказала: "Привет!"')
print('''Она сказала: "Привет!"''')

#Задание 3

print('Список дел:\n\tУчеба\n\tУборка\n\tСпорт')

#Задание 4

distance, speed = int(input('Введите ваше расстояние (в км): ')),\
                  int(input('Введите ваш скорость (в км/ч): '))
time = round(distance / speed, 1)
print('Время в пути:', time, 'часов')

#Задание 4.1

distance, speed = int(input('Введите ваше расстояние (в км): ')),\
                  int(input('Введите вашу скорость (в км/ч): '))
time_total = int(distance / speed * 60)
hours = time_total // 60
minutes = time_total % 60
print('Время в пути:', hours, 'часов', minutes, 'минут')

#Задание 5

days = int(input('Введите количество дней до события: '))
weeks = days // 7
amount_days = days % 7
print('До события осталось:', weeks, 'недель', amount_days, 'дней')

#Задание 6

distance, fuel, price = int(input('Введите расстояние (в км): ')),\
                        int(input('Введите расход бензина на 100 км: ')),\
                        int(input('Введите цену за литр бензина: '))
total_price = (distance / 100) * fuel * price
print('Стоимость бензина для поездки', total_price)

#Задание 7

tasks = int(input("Введите количество задач: "))
time_per_task = int(input("Введите среднее время выполнения одной задачи (мин):"))
total_minutes = tasks * time_per_task
hours = total_minutes // 60
minutes = total_minutes % 60
print("Общее время:", hours, "часа и", minutes, "минут")

#Задание 8

n = int(input("Enter the number: "))
nn = n + n*10
nnn = nn + n*100
print("Значение выражения:", n + nn + nnn)

n = input("Введите число: ")
nn = n + n
nnn = n + n + n
result = int(n) + int(nn) + int(nnn)
print("Значение выражения:", result)

#Задание 9
# Напишите программу, которая считывает четырёхзначное число и меняет местами
# первую и последнюю цифры.
n = int(input("Enter the 4-digit number: "))
first_digit = n // 1000
second_digit = (n // 100) % 10
third_digit = (n % 100) // 10
fourth_digit = n % 10
new_n = str(fourth_digit) + str(second_digit) + str(third_digit) + str(first_digit)
print("Число после изменения:", new_n)

number = input("Введите четырёхзначное число: ")
n = int(number)
first_digit = n // 1000
last_digit = n % 10
middle_part = (n % 1000) // 10
new_number = last_digit * 1000 + middle_part * 10 + first_digit
#print("Число после изменения:", new_number)
print(first_digit, last_digit, middle_part, new_number)
