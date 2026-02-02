# Task 1
value1 = bool(int(input('Enter value 1: ')))
value2 = bool(int(input('Enter value 2: ')))
print("and:", value1 and value2)
print("or:", value1 or value2)
print("not:", not value1)
print("equal:", value1 == value2)
print("not equal:", value1 != value2)

# Task 2
is_light_on = bool(int(input("Свет включён? ")))
is_window_open = bool(int(input("Окно открыто? ")))
print("Оба условия выполнены?", is_light_on and is_window_open)
print("Хотя бы одно условие выполнено?", is_light_on or is_window_open)

# Task 3
base_tarif = 30
limit_mb = 500
extra_price_per_mb = 0.2

used_mb = int(input("Введите использованные мегабайты: "))

extra_mb = max(0, used_mb - limit_mb)
#or extra_mb = (used_mb - limit_mb) * (used_mb > limit_mb)
extra_cost = extra_mb * extra_price_per_mb

total_cost = base_tarif + extra_cost

print("Общая стоимость:", total_cost)

