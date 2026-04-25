# task1 - Извлечение дат
import re
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
pattern = r"\b\d{2}[\/\-.]\d{2}[\/\-.]\d{4}\b"
dates = re.findall(pattern, text)
for date in dates:
    print(date)

# valid date or not
# from datetime import datetime
# valid_dates = []
# for date_str in dates:
#     sep = re.search(r"[\/\-.]", date_str).group()
#     try:
#         day, month, year = date_str.split(sep)
#         dt = datetime(int(year), int(month), int(day))
#         valid_dates.append(date_str)
#     except ValueError:
#         pass
#
# for valid_date in valid_dates:
#     print(valid_date)

# task2 - Разделение списка тегов
import re

tag_input = "python, data-science / machine-learning; AI\nneural-networks"
tags = re.split(r"[,\s;/]+", tag_input)
print(tags)