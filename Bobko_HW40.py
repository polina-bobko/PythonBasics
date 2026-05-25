# task 1 - Электронное письмо
from datetime import datetime
class Email:
    """
    Класс, представляющий электронное письмо.
    """
    def __init__(self, sender: str, recipient: str, subject: str, body: str, date: datetime):
        """
        Создание объекта Email.

        :param sender: адрес отправителя (str)
        :param recipient: адрес получателя (str)
        :param subject: тема письма (str)
        :param body: текст письма (str)
        :param date: дата отправки (datetime)
        """
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self) -> str:
        """
        Строковое представление письма.

        :return: форматированная строка письма (str)
        """
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __len__(self) -> int:
        """
        Длина текста письма (body без пробелов по краям).

        :return: количество символов в тексте письма (int)
        """
        return len(self.body.strip())

    def __bool__(self) -> bool:
        """
        Проверка, содержит ли письмо текст (не пустое и не только пробелы).

        :return: True если есть содержимое, иначе False
        """
        return bool(self.body and self.body.strip())

    def __eq__(self, other) -> bool:
        """
        Сравнение писем по дате на одну и ту же дату.

        :param other: другое письмо (Email)
        :return: True если текущее письмо с той же датой, что и другое
        """
        if not isinstance(other, Email):
            return NotImplemented
        return self.date == other.date

    def __gt__(self, other) -> bool:
        """
        Сравнение писем по дате (новее > старее).

        :param other: другое письмо (Email)
        :return: True если текущее письмо новее
        """
        if not isinstance(other, Email):
            return NotImplemented
        return self.date > other.date

e1 = Email(
    "alice@example.com",
    "bob@example.com",
    "Meeting",
    "Let's meet at 10am",
    datetime(2024, 6, 10)
)

e2 = Email(
    "bob@example.com",
    "alice@example.com",
    "Report",
    "",
    datetime(2024, 6, 11)
)

print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)

# task 2 - Класс для работы с деньгами
class Money:
    """
    Класс, представляющий денежную сумму.
    """
    def __init__(self, amount: float):
        """
        Создание объекта Money.

        :param amount: начальная сумма (int или float)
        """
        self.amount = amount

    @property
    def amount(self) -> float:
        """
        Получение текущей суммы.

        :return: значение суммы (float)
        """
        return self._amount

    @amount.setter
    def amount(self, value: float):
        """
        Установка суммы с валидацией.

        :param value: новая сумма (int или float)
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Amount must be int or float")
        self._amount = value

    def __str__(self) -> str:
        """
        Строковое представление объекта.

        :return: строка вида $<amount>
        """
        return f"${self.amount}"

    def __add__(self, other: "Money") -> "Money":
        """
        Сложение двух объектов Money.

        :param other: второй объект Money
        :return: новый объект Money с суммой сложения
        """
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __sub__(self, other: "Money") -> "Money":
        """
        Вычитание двух объектов Money.

        :param other: второй объект Money
        :return: новый объект Money (не ниже 0)
        """
        if not isinstance(other, Money):
            return NotImplemented
        result = self.amount - other.amount
        return Money(max(0, result))

money1 = Money(100)
money2 = Money(50)

print(money1 + money2)  # $150
print(money1 - money2)  # $50
print(money2 - money1)  # $0