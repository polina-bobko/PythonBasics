# task 1 - Деление без ошибок
def division(dividend: float, divisor: float) -> float:
    """
    Выполняет деление двух чисел.

    :param dividend: Делимое типа float.
    :param divisor: Делитель типа float.
    :return: Результат деления dividend на divisor типа float.
    """
    return dividend / divisor

try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    result = division(a, b)
    print(result)
except ZeroDivisionError:
    print("Деление на ноль невозможно.")
except ValueError:
    print("Введено некорректное число.")
except Exception:
    print("Произошла непредвиденная ошибка.")

# task 2 - Логирование ошибок
import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
)

def division(dividend: float, divisor: float) -> float:
    """
    Выполняет деление двух чисел.

    :param dividend: Делимое типа float.
    :param divisor: Делитель типа float.
    :return: Результат деления dividend на divisor типа float.
    """
    return dividend / divisor

try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    result = division(a, b)
    print(result)
except ZeroDivisionError:
    logging.error("Ошибка: Деление на ноль невозможно.")
except ValueError:
    logging.error("Ошибка: Введено некорректное число.")
except Exception:
    logging.error("Ошибка: Произошла непредвиденная ошибка.")