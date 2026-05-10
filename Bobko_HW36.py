# task 1 - Класс Person
class Person:
    def __init__(self, name: str) -> None:
        """
        Инициализирует объект человека.

        :param name: Имя человека
        """
        self.name = name

    def introduce(self) -> str:
        """
        Выводит приветствие с именем человека.

        :return Строка с приветствием и представлением.
        """
        return f"Hello, my name is {self.name}."


person = Person("Alice")
print(person.introduce())

# task 2 - Класс Student
class Student(Person):
    def __init__(self, name: str, course: int) -> None:
        """
        Инициализирует объект студента.

        :param name: Имя студента
        :param course: Номер курса
        """
        super().__init__(name)
        self.course = course

    def introduce(self) -> str:
        """
        Выводит приветствие и номер курса студента.

        :return Строка с приветствием и представлением и с номером курса.
        """
        return f"{super().introduce()}\nI'm on course {self.course}."


student1 = Student("Alice", 2)
print(student1.introduce())

# task 3 - Класс Teacher и список людей
class Teacher(Person):
    def __init__(self, name: str, subject: str) -> None:
        """
        Инициализирует объект преподавателя.

        :param name: Имя преподавателя
        :param subject: Название предмета
        """
        super().__init__(name)
        self.subject = subject

    def introduce(self) -> str:
        """
        Выводит информацию о преподавателе и его предмете.

        :return Строка с представлением профессора и его предмет.
        """
        return f"Hello, I am professor {self.name}. \nMy subject is {self.subject}."

teacher = Teacher("Bob", "Mathematics")

print(teacher.introduce())

print(50*"-")

student2 = Student("Dana", 3)

people = [student1, student2, teacher]

for person in people:
    print(person.introduce())
