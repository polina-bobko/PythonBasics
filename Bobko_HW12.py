# Task1. Сумма положительных чисел
numbers = input("Enter the numbers: ")
#numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
list_nums = numbers.split()
sum = 0
for n in list_nums:
    n = float(n)
    if n > 0:
        sum += n

print(f"Сумма положительных чисел: ${sum:,.2f}")

# Task2. Счета клиентов
data_list = [
    "John 23 12345.678",
    "Alice 30 200.50",
    "Bob 35 15000.3",
    "Charlie 40 500.75"]

for s in data_list:
    person = s.split()
    name = person[0]
    age = person[1]
    balance = float(person[2])
    print(f"Name: {name:<10} | Age: {age:>3} | Balance: {balance:>10.2f}")

#     name, age, balance = s.split()
#     print(f"Name: {name:<10} | Age: {age:>3} | Balance: {float(balance):>10.2f}")
