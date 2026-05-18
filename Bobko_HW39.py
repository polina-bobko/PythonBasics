# task 1 - Фигуры и площади

# task 2 - Проверка размеров фигур

from abc import ABC, abstractmethod
import math


class InvalidSizeError(Exception):
    """
    Исключение, возникающее при передаче
    некорректного размера фигуры.
    """
    pass


class Shape(ABC):
    """
    Абстрактный базовый класс для геометрических фигур.

    Methods:
        area() -> float:
            Возвращает площадь фигуры.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры.

        Returns:
            float: площадь фигуры.
        """
        pass


class Circle(Shape):
    """
    Класс круга.

    Attributes:
        radius (float):
            Радиус круга. Должен быть положительным числом.

    Methods:
        area() -> float:
            Возвращает площадь круга.
    """

    def __init__(self, radius: float) -> None:
        """
        Инициализирует объект Circle.

        Args:
            radius (float):
                Радиус круга.

        Raises:
            InvalidSizeError:
                Если радиус меньше или равен нулю.
        """
        self.radius = radius

    @property
    def radius(self) -> float:
        """
        Получает значение радиуса.

        Returns:
            float: радиус круга.
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """
        Устанавливает значение радиуса.

        Args:
            value (float):
                Новое значение радиуса.

        Raises:
            InvalidSizeError:
                Если значение меньше или равно нулю.
        """
        if value <= 0:
            raise InvalidSizeError("Radius must be positive")
        self._radius = value

    def area(self) -> float:
        """
        Вычисляет площадь круга.

        Formula:
            π * r²

        Returns:
            float: площадь круга.
        """
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """
    Класс прямоугольника.

    Attributes:
        width (float):
            Ширина прямоугольника.
        height (float):
            Высота прямоугольника.

    Methods:
        area() -> float:
            Возвращает площадь прямоугольника.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Инициализирует объект Rectangle.

        Args:
            width (float):
                Ширина прямоугольника.
            height (float):
                Высота прямоугольника.

        Raises:
            InvalidSizeError:
                Если width или height меньше
                или равны нулю.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        """
        Получает ширину прямоугольника.

        Returns:
            float: ширина прямоугольника.
        """
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        """
        Устанавливает ширину прямоугольника.

        Args:
            value (float):
                Новое значение ширины.

        Raises:
            InvalidSizeError:
                Если значение меньше или равно нулю.
        """
        if value <= 0:
            raise InvalidSizeError("Width must be positive")
        self._width = value

    @property
    def height(self) -> float:
        """
        Получает высоту прямоугольника.

        Returns:
            float: высота прямоугольника.
        """
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """
        Устанавливает высоту прямоугольника.

        Args:
            value (float):
                Новое значение высоты.

        Raises:
            InvalidSizeError:
                Если значение меньше или равно нулю.
        """
        if value <= 0:
            raise InvalidSizeError("Height must be positive")
        self._height = value

    def area(self) -> float:
        """
        Вычисляет площадь прямоугольника.

        Formula:
            width * height

        Returns:
            float: площадь прямоугольника.
        """
        return self.width * self.height


shapes = [Circle(3), Rectangle(4, 5)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")