# Одно слово
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
one_words_list = []
for st in text_list:
    if " " not in st:
        one_words_list.append(st.lower())
print(one_words_list)

# Обновление цен товаров
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount = int(input("Введите скидку (в процентах): "))
print(f"{'Товар':<15}{'Старая цена':^15}{'Новая цена':<15}")
for item in products:
    product, price = item
    new_price = price-discount*price/100
    print(f"{product:<15}{(f'{price:.2f}$'):^15}{(f'{new_price:.2f}$'):<15}")