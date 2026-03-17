# Повторения букв
from collections import Counter

def count_letters_in_text(text):
    return dict(Counter(c for c in text.lower() if c.isalpha()))


text = "Programming is fun!"
print(count_letters_in_text(text))


# from collections import OrderedDict
#
# def count_letters(text):
#     result = OrderedDict()
#     for char in text.lower():
#         if char.isalpha():
#             result[char] = result.get(char, 0) + 1
#     return result
#
# print(count_letters(text))

# Группировка студентов по классам
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
#{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}
from collections import defaultdict
dd = defaultdict(list)
for key, student in students:
        dd[key].append(student)

print(dict(dd))