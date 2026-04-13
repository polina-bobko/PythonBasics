# task1
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

def get_selected_orders(orders_list: list, min_price: int = 500) -> list:
    filtered = filter(lambda order: order["price"] > min_price, orders_list)
    products = map(lambda order: order["product"], filtered)
    return sorted(products)

tasks = get_selected_orders(orders)
# tasks = get_selected_orders(orders, 1000)
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