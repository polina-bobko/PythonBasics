task_level = 10
match task_level:
    case 1:
        print("Упорядочить числа по возрастанию")
        a = int(input('Введите первое число: '))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        print('Числа упорядочены ' if a < b < c else 'Числа не упорядочены')
    case 2:
        print('Большее число')
        a = int(input('Введите первое число: '))
        b = int(input("Введите второе число: "))
        if a == b:
            print('Числа равны')
        elif a > b:
            print('Большее число', a)
        else:
            print('Большее число', b)
    case 3:
        print('Определение четности числа')
        a = int(input('Введите число: '))
        print('Нечетное' if a % 2 else 'Четное')
    case 4:
        print('Категории возраста')
        a = int(input('Введите возраст: '))
        if a < 12:
            print('Ребенок')
        elif a < 18:
            print('Подросток')
        elif a < 60:
            print('Взрослый')
        else:
            print('Пожилой')
    case 5:
        print('Существование треугольника')
        a = int(input('Введите первое число: '))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        print('Такой треугольник может существовать:', a + b > c and a + c > b and b + c > a)
    case 6:
        print('Пустая строка')
        print('не пустая строка' if input('Введите строку:') else 'Пустая строка')
    case 7:
        print('Определение квадранта')
        x = int(input('Введите координату x: '))
        y = int(input("Введите координату y: "))
        if x > 0 and y > 0:
            print('1-квадрант')
        elif x < 0 < y:
            print('2-квадрант')
        elif x < 0 and y < 0:
            print('3-квадрант')
        elif x > 0 > y:
            print('4-квадрант')
        else:
            print('НЕ в квадранте')
    case 8:
        print('Допустимые значение времени')
        h = int(input('Введите часы: '))
        m = int(input("Введите минуты: "))
        print('Время правильное' if 0 <= h < 24 and 0 <= m < 60 else 'Некорректное время')
    case 9:
        print('Знак произведения')
        a = int(input('Введите первое число: '))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        # print('Произведение положительное' if (a / b / c) > 0 else  'Отрицательное')
        s = (a < 0) + (b < 0) + (c < 0)
        print(s)
        if a == 0 or b == 0 or c == 0:
            print('Произведение равно 0')
        elif s % 2 == 0:
            print('Произведение положительное')
        else:
            print('Отрицательное')
    case 10:
        print('Расчет налога')
        salary = int(input('Введите доход: '))
        if salary <= 10000:
            tax = salary * 0.05
        elif salary <= 50000:
            tax = 500 + (salary - 10000) * 0.1
        else:
            tax = 500 + 40000*0.1 + (salary - 50000) * 0.2
        print('Налог: ', tax)
        print('Итоговая сумма после уплаты налога: ', salary - tax)