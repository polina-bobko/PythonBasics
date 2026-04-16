#task1 Принимать аргументы командной строки:
# python sales_report.py <input_file> <output_directory>
# Где:
# ○ <input_file> — путь к входному файлу с продажами.
# ○ <output_directory> — папка, куда будут сохранены отчёты.
from collections import defaultdict
import os
import sys
# input_file = sys.argv[1]
# output_dir = sys.argv[2]
# with open(input_file, 'r', encoding='utf-8') as f:

#task2 Считать данные из текстового файла, в котором каждая строка содержит информацию в следующем формате:
# имя,дата,сумма,категория,город
# Пример входных данных:
# Olivia Suarez,2024-08-02,4565,Electronics,Dallas
# Jennifer Jacobs,2023-08-19,4963,Automotive,London
# Erin Johnson,2024-08-29,1796,Clothing,Miami

# with open(input_file, 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)

#task3 Сгруппировать данные по годам и месяцам, создавая для каждого года и месяца отдельную папку в указанной директории.
def read_data(input_file):
    sales = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            name, date, amount, category, city = line.split(',')
            year, month, _ = date.split('-')
            sales.append({
                'name': name.strip(),
                'date': date.strip(),
                'amount': float(amount),
                'category': category.strip(),
                'city': city.strip(),
                'year': int(year),
                'month': int(month),
            })
    return sales


def grouped_by_category(sales):
    grouped_sales = defaultdict(int)
    for sale in sales:
        grouped_sales[sale['category']] += sale['amount']
    return grouped_sales


def grouped_by_year_month(sales):
    grouped_sales = defaultdict(list)
    for sale in sales:
        key = (sale["year"], sale["month"])
        grouped_sales[key].append(sale)
    return grouped_sales


def generate_reports(grouped_sales):
    output_file = 'reports.txt'
    for key, value in grouped_sales.items():
        year, month = key
        path_file = os.path.join(str(year), str(month), output_file)

        os.makedirs(os.path.dirname(path_file), exist_ok=True)

        with open(path_file, 'w', encoding='utf-8') as f:
            for sale in value:
                f.write(
                    f"{sale['name']}-{sale['date']}-{sale['amount']}-{sale['category']}-{sale['city']}\n"
                )


data = read_data('sales_data.txt')
print(*data, sep='\n')
print('-' * 20)
categories = grouped_by_category(data)
print(*categories.items(), sep='\n')
print('-' * 20)
month = grouped_by_year_month(data)
print(*month.items(), sep='\n')
generate_reports(month)

# import os
# with open(input_file, 'r', encoding='utf-8') as f:
#     for line in f:
#         split_line = line.split(',')
#         name, date, amount, category, city = split_line
#         year, month, _ = date.split('-')
#         os.makedirs(os.path.join(output_dir, year, month), exist_ok=True)
#         with open(os.path.join(output_dir, year, month, 'employees_sales'), 'a', encoding='utf-8') as fi:
#             fi.write(f'{line}')
#
# #task4 Cоздать общий отчёт по каждому месяцу (monthly_report.txt), в котором указана суммарная выручка по каждой категории и общая сумма:
# # Automotive,109539
# # Books,133160
# # Clothing,102001
# # Electronics,79403
# # Groceries,104387
# # Home Appliances,99911
# # Sports,78782
# # Full,707183
#
# with open(input_file, 'r', encoding='utf-8') as f:
#     for line in f:
#         split_line = line.split(',')
#         name, date, amount, category, city = split_line
#         year, month, _ = date.split('-')
#         os.makedirs(os.path.join(output_dir, year, month), exist_ok=True)
#         with open(os.path.join(output_dir, year, month, 'employees_sales'), 'a', encoding='utf-8') as fi:
#             fi.write(f'{line}')