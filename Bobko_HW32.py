# task 1 - Фабрика функций округления
from typing import Callable


def make_rounder(rounded_up_to_num: int) -> Callable[[float | int], float]:
    """
    Создаёт функцию для округления чисел до указанного количества знаков.

    :param rounded_up_to_num: Количество знаков после запятой для округления.
    :return: Функция, принимающая число и возвращающая округлённое значение.
    """

    def wrapper(num: float | int) -> float:
        """
        Округляет переданное число до заданного количества знаков.

        :param num: Число для округления.
        :return: Округлённое число.
        """
        return round(num, rounded_up_to_num)

    return wrapper


round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

# task 2 - Расширяемый логгер событий
from datetime import datetime
from typing import Callable


def create_logger() -> Callable[[str | None], list[str]]:
    """
    Создаёт логгер событий.

    :return: Функция-логгер, сохраняющая события и возвращающая список событий.
    :rtype: Callable[[str | None], list[str]]
    """

    events = []

    def log(message: str | None = None) -> list[str]:
        """
        Сохраняет событие с текущим временем.

        :param message: Сообщение события.
        :return: Список всех сохранённых событий.
        """
        if message:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"{message}: {current_time}")

        return events

    return log


log = create_logger()

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for event in log():
    print(event)

# task 3 - Рамка вокруг вывода

from typing import Callable

def frame(func: Callable) -> Callable:
    """
    Создаёт рамку вокруг результата функции.

    :param func: Функция, вывод которой нужно обернуть рамкой.
    :return: Обёрнутая функция.
    """

    def wrapper() -> str:
        """
        Выводит рамку до и после вызова функции.

        :return: Отформатированная строка с рамкой
        """
        return f"{50 * '-'}\n{func()}\n{50 * '-'}"

    return wrapper


def say_hello() -> str:
    """
    Выводит приветствие.

    :return Строка с приветствием
    """
    return "Привет, игрок!"


hello = frame(say_hello)

print(hello())