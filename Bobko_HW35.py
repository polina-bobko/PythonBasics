# task 1 - Счётчик экземпляров
class User:
    total_users = 0

    def __init__(self, username: str, password: str) -> None:
        """
        Создаёт нового пользователя.

        :param username: Логин пользователя
        :param password: Пароль пользователя
        """
        self.username = username
        self.password = password

        User.total_users += 1

    @classmethod
    def get_total(cls) -> int:
        """
        Возвращает общее количество созданных пользователей.

        :return: Количество пользователей (целое число)
        """
        return cls.total_users


user1 = User("Ivan", "QWerty123")
user2 = User("Persik", "12345689")
user3 = User("Dynka", "p@ssw0rd123")

print("Total users:", User.get_total())

# task 2 - Проверка данных пользователя
class User:
    total_users = 0

    def __init__(self, username: str, password: str) -> None:
        """
        Создаёт нового пользователя с проверкой данных.

        :param username: Имя пользователя (непустая строка)
        :param password: Пароль (строка длиной не менее 5 символов)
        """
        if not isinstance(username, str) or not username.strip():
            raise ValueError(f"Invalid username: '{username}'")
        if not isinstance(password, str) or len(password) < 5:
            raise ValueError(f"Invalid password: '{password}'")

        self.username = username
        self.password = password

        User.total_users += 1

    @classmethod
    def get_total(cls) -> int:
        """
        Возвращает количество созданных пользователей.

        :return: Количество пользователей
        """
        return cls.total_users

    def __str__(self) -> str:
        """
        Возвращает строковое представление пользователя.

        :return: Строка формата 'User: username'
        """
        return f"User: {self.username}"


try:
    user1 = User("Alice", "string")
    print(user1)

    user2 = User("Bob", "qwe")
    print(user2)

except ValueError as error:
    print(f"ValueError: {error}")