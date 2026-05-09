# task 1 - Класс Rectangle
class Rectangle:
    def __init__(self, width: float, height: float):
        """
        Инициализирует прямоугольник.

        :param width: Ширина
        :param height: Высота
        """
        if width <= 0:
            raise ValueError("Ширина должна быть больше нуля!")
        if height <= 0:
            raise ValueError("Высота должна быть больше нуля!")
        self.width = width
        self.height = height

    def get_area(self) -> float:
        """
        Считает и возвращает площадь прямоугольника.

        :return Площадь прямоугольника (тип - float)
        """
        return self.width * self.height


rect = Rectangle(4, 5)

print(f"Площадь: {rect.get_area()}")

new_width = 5
new_height = 7

if new_width <= 0:
    raise ValueError("Ширина должна быть больше нуля!")
if new_height <= 0:
    raise ValueError("Высота должна быть больше нуля!")

rect.width = new_width
rect.height = new_height

print(f"Новая площадь: {rect.get_area()}")

# task 2 - Класс Counter
class Counter:
    def __init__(self, value: int = 0) -> None:
        """
        Инициализирует счётчик.

        :param value: Начальное значение счётчика (целое число, не меньше 0)
        """
        if not isinstance(value, int):
            raise TypeError("Начальное значение должно быть целым числом")

        if value < 0:
            raise ValueError("Начальное значение должно быть неотрицательным")

        self.value = value

    def increment(self) -> str:
        """
        Увеличивает значение счётчика на 1.

        :return: Строка с новым увеличенным значением.
        """
        self.value += 1
        return f"Значение увеличено, текущее: {self.value}"

    def decrement(self) -> str:
        """
        Уменьшает значение счётчика на 1.

        :return: Строка с новым уменьшенным значением.
        """
        self.value -= 1
        return f"Значение уменьшено, текущее: {self.value}"

    def get_value(self) -> int:
        """
        Возвращает текущее состояние счётчика.

        :return: Строка с текущим значением.
        """
        return self.value


counter = Counter()

print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.decrement())

print(f"Текущее значение: {counter.get_value()}")