# task1 - План по дням недели
import itertools
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

days = list(weekly_schedule.keys())
day_iterator = itertools.cycle(days)

while True:
    user_input = input("Нажмите 'Enter' для получения плана: ")
    if user_input.lower() == 'q':
        break
    day = next(day_iterator)
    tasks = weekly_schedule[day]
    print(f"{day}: {', '.join(tasks)}")

# task2 - Объединение списков продуктов
import itertools
from typing import Iterator

def merge_products(*lists: list[str]) -> Iterator[str]:
    """
    Принимает несколько списков с названиями продуктов и возвращает генератор,
    который последовательно выдаёт все элементы из этих списков в нижнем регистре.

    Args: *lists (list[str]): произвольное количество списков строк с продуктами.
    Returns: Iterator[str]: генератор строк в нижнем регистре.
    """
    return (item.lower() for item in itertools.chain(*lists))


fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

gen = merge_products(fruits, vegetables, dairy)

for product in gen:
    print(product)

# task3 - Комбинации одежды
import itertools
from typing import Iterator

def generate_outfits(
    clothes: list[str],
    colors: list[str],
    sizes: list[str]
) -> Iterator[str]:
    """
    Генерирует все возможные комбинации одежды, цветов и размеров
    в формате "Clothe - Color - Size".

    Args:
        clothes (list[str]): типы одежды
        colors (list[str]): цвета
        sizes (list[str]): размеры
    Returns: Iterator[str]: генератор строк с комбинациями
    """
    return (
        f"{clothe} - {color} - {size}"
        for clothe, color, size in itertools.product(clothes, colors, sizes)
    )

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

gen = generate_outfits(clothes, colors, sizes)

for item in gen:
    print(item)