# task 1 - Банковский счёт
class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        """
        Инициализирует банковский счёт.

        :param owner: Имя владельца счёта
        :param balance: Начальный баланс
        """
        self.owner = owner
        self.balance = balance

    @property
    def balance(self) -> float:
        """
        Геттер для получения баланса.
        """
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        """
        Сеттер для установки баланса.
        Разрешает только int и float.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be int or float.")

        self.__balance = float(value)

    def deposit(self, amount: float) -> float | str:
        """
        Пополнение счёта.

        :param amount: Сумма пополнения
        :return: Новый баланс или сообщение об ошибке
        """
        if not isinstance(amount, (int, float)):
            return "Error: Amount must be int or float."

        if amount <= 0:
            return "Error: Amount must be positive."

        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float) -> float | str:
        """
        Снятие средств.

        :param amount: Сумма снятия
        :return: Новый баланс или сообщение об ошибке
        """
        if not isinstance(amount, (int, float)):
            return "Error: Amount must be int or float."

        if amount <= 0:
            return "Error: Amount must be positive."

        if amount > self.__balance:
            return "Error: Not enough funds."

        self.__balance -= amount
        return self.__balance

    def show_balance(self) -> float:
        """
        Отображает текущий баланс.

        :return: Баланс
        """
        return self.__balance


account = BankAccount("Polina", 150)

print("Current balance:", account.show_balance())
# account.balance = "hello"  # TypeError

print(account.withdraw(-1))
print(account.withdraw(500))

print("Current balance:", account.show_balance())


# task 2 - История операций
class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self.balance = balance
        self.__history = []

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be int or float.")

        self.__balance = float(value)

    @property
    def history(self) -> list[str]:
        return self.__history.copy()

    def deposit(self, amount: float) -> float | str:
        if not isinstance(amount, (int, float)):
            return "Error: Amount must be int or float."

        if amount <= 0:
            return "Error: Amount must be positive."

        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

        return self.__balance

    def withdraw(self, amount: float) -> float | str:
        if not isinstance(amount, (int, float)):
            return "Error: Amount must be int or float."

        if amount <= 0:
            return "Error: Amount must be positive."

        if amount > self.__balance:
            return "Error: Not enough funds."

        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

        return self.__balance

    def show_balance(self) -> float:
        return self.__balance


account = BankAccount("Polina")

print("Balance updated:", account.deposit(150))
print("Balance updated:", account.withdraw(100))

print("Current balance:", account.show_balance())

print("Operation history:")
for operation in account.history:
    print(operation)