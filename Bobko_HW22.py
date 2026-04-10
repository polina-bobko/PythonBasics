# task1
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

# Отбирает заказы дороже 500.
# Создаёт список названий отобранных продуктов в алфавитном порядке.
# Возвращает итоговый список названий.

def get_selected_orders(orders_list: list) -> list:
    filtered = list(filter(lambda x: x["price"] > 500, orders_list))
    return sorted(map(lambda x: x["product"], filtered))
tasks = get_selected_orders(orders)
print(tasks)

# task2
# Вычисляет общую выручку для каждого товара.
# Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

from functools import reduce

revenue = reduce(
    lambda acc, item: acc.update({item[0]: item[1]*item[2]}) or acc,
    sales,
    {}
)
sorted_revenue = dict(sorted(revenue.items(), key=lambda x: x[1], reverse=True))

print(sorted_revenue)