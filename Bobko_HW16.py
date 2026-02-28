# Оценки текстом
grades = [5, 3, 4, 2, 1, 5, 3]
grades_list = [[g, 'отлично'] if g == 5 else ([g, 'хорошо'] if 3 <= g < 5
                                              else [g,'неудовлетворительно']) for g in grades]
print(grades_list)

# grades = [5, 3, 4, 2, 1, 5, 3]
# descriptions = [
#     'отлично' if g == 5
#     else 'хорошо' if 3 <= g < 5
#     else 'неудовлетворительно'
#     for g in grades
# ]
# grades_list = [[g, desc] for g, desc in zip(grades, descriptions)]
# print(grades_list)

# Правильные скобки
string_with_brackets = input("Скобки: ")
open_brackets = "([{"
close_brackets = ")]}"
stack = []

for ch in string_with_brackets:
    if ch in open_brackets:
        stack.append(ch)
    elif ch in close_brackets:
        if not stack:
            is_valid = False
            break
        if (ch == ')' and stack[-1] == '(') or \
           (ch == ']' and stack[-1] == '[') or \
           (ch == '}' and stack[-1] == '{'):
            stack.pop()
        else:
            is_valid = False
            break
else:
    is_valid = not stack

print("Валидны:", is_valid)

# valid = True
# for ch in string_with_brackets:
#     if ch in open_brackets:
#         stack.append(ch)
#     elif ch in close_brackets:
#         if not stack or open_brackets.index(stack[-1]) != close_brackets.index(ch):
#             valid = False
#             break
#         stack.pop()
#
# if stack:
#     valid = False
#
# print("Валидны:", valid)