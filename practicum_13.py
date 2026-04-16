# import os
# from collections import defaultdict
#
#
# sales_data = "sales_data.txt"
# output_dir = "reports"
# os.makedirs(output_dir, exist_ok=True)
# structure = defaultdict(list)
#
# with open(sales_data) as f:
#     for line in f:
#         name, date, sales_sum, category, city = line.split(",")
#         structure[date[:7]].append((date, name,sales_sum, category, city))
#
# filename = "monthly_report.txt"
# for data, value in structure.items():
#     year, month = data.split("-")
#     path = os.path.join(output_dir, year, month)
#     os.makedirs(path, exist_ok=True)
#
#     sum_mon = defaultdict(float)
#     category_sum = defaultdict(list)
#     for date, name, sales_sum, category, city in value:
#         sum_mon[category] += float(sales_sum)
#         category_sum[category].append((date, name, sales_sum))
#
#     for key, value in category_sum.items():
#         with open(os.path.join(path, key + ".txt"), "w") as f:
#             for date, name, sales_sum in sorted(value):
#                 f.write(f"{date}, {name}, {sales_sum}\n")
#
#
#     with open(os.path.join(path, filename), "w") as f:
#         for key, value in sum_mon.items():
#             f.write(f"{key}, {value}\n")







import os
import sys
from collections import defaultdict


def read_sales_data(file_path):
    """Считывает данные из .txt файла и возвращает список записей."""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    sales = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            name, date, amount, category, city = parts
            year, month, day = date.split("-")
            sales.append({
                "name": name,
                "date": date,
                "amount": int(amount),
                "category": category,
                "year": year,
                "month": month,
                "day": day,
            })
    return sales


def write_category_reports(output_dir, grouped_sales):
    """Создаёт файлы с отчётами по категориям в формате 'дата, продавец,
   сумма', сортируя по дате."""
    for (year, month, category), records in grouped_sales.items():
        category_file = os.path.join(output_dir, year, month, f"{category}.txt")
        os.makedirs(os.path.dirname(category_file), exist_ok=True)
        # Сортируем по дате
        sorted_records = sorted(records, key=lambda x: x["date"])
        with open(category_file, "w", encoding="utf-8") as file:
            for record in sorted_records:
                file.write(f"{record['date']},{record['name']},{record['amount']}\n")

def write_monthly_reports(output_dir, category_totals):
    """Создаёт общий отчёт по каждому месяцу с суммами продаж по категориям."""
    for (year, month), category_sums in category_totals.items():
        report_file = os.path.join(output_dir, year, month,
                                   "monthly_report.txt")
        os.makedirs(os.path.dirname(report_file), exist_ok=True)
        with open(report_file, "w", encoding="utf-8") as file:
            for category, total in sorted(category_sums.items()):
                file.write(f"{category},{total}\n")
            file.write(f"Full,{sum(category_sums.values())}\n")

def process_sales_data(file_path, output_dir):
    """Обрабатывает продажи и создаёт отчёты по категориям и общие отчёты по
   месяцам."""
    sales = read_sales_data(file_path)
    grouped_sales = defaultdict(list)
    category_totals = defaultdict(lambda: defaultdict(int))
    print(len(sales))
    for record in sales.copy():
        key = (record["year"], record["month"], record["category"])
        grouped_sales[key].append(record.copy())
        category_totals[(record["year"], record["month"])][record["category"]] += record["amount"]
    write_category_reports(output_dir, grouped_sales)
    write_monthly_reports(output_dir, category_totals)
# if len(sys.argv) < 3:
#     print("Usage: python script.py <input_file> <output_directory>")
#     sys.exit(1)

input_file = "sales_data.txt"
output_directory = "reports1"
process_sales_data(input_file, output_directory)
print("Reports generated successfully!")