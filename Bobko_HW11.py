# Task1. Звёздочки вместо чисел
text = input("Enter the text: ")
# new_text = ""
# for ch in text:
#     if ch.isdigit():
#         new_text += '*'
#     else:
#         new_text += ch
# print("String:", text)
# print("Result:", new_text)

result = []
for ch in text:
    if ch.isdigit():
        result.append('*')
    else:
        result.append(ch)

new_text = ''.join(result)
print("String:", text)
print("Result:", new_text)

# Task2. Количество символов
text1 = input("Enter the text: ")
text_lower = text1.lower()
print("Text:", text1)
#text = "Programming in python"
chars = []
for char in text_lower:
    if char not in chars:
        chars.append(char)
for char in chars:
    if text_lower.count(char) > 1:
        print(f"Символ '{char}' встречается {text_lower.count(char)} раз(а)")

# Task3. Увеличение чисел
text2 = input("Enter the text: ")
#text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
words_in_text = text2.split()
list = []
for word in words_in_text:
    if word.isnumeric() or word.count(".")==1 and word.replace('.', '').isdigit():
        word = float(word)*10
        list.append(str(word))
    else:
        list.append(word)
print(' '.join(list))