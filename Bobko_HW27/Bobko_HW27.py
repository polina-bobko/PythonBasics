# task1 - Фильтрация по ключевому слову
import os

file = input('Enter the file name: ')
keyword = input('Enter the keyword: ')

def filter_file_by_keyword(file_name: str, key_word: str) -> str | None:
    """
    Ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.

    :param file_name: Имя исходного файла со строками.
    :param key_word: Ключевое слово. По нему производится поиск/фильтрация подходящих строк в файле.
    :return: Имя нового файла или None, если совпадений нет.
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError("Файл не существует.")
    new_file_name = f'{key_word}_{file_name}'

    filtered_lines = []

    with open(file_name, "r", encoding="utf-8") as origin_file:
        for line in origin_file:
            if key_word.lower() in line.lower():
                filtered_lines.append(line)

    if not filtered_lines:
        return None

    with open(new_file_name, "w", encoding="utf-8") as new_file:
        new_file.writelines(filtered_lines)

    return new_file_name

try:
    result = filter_file_by_keyword(file, keyword)
    if result is None:
        print("Совпадения не найдены. Новый файл не создан.")
    else:
        print(f"Строки сохранены в файл: {result}")
except FileNotFoundError as error:
    print(error)
except PermissionError:
    print("Ошибка доступа к файлу.")
except UnicodeDecodeError:
    print("Ошибка кодировки файла.")
except OSError as error:
    print(f"Системная ошибка: {error}")
except Exception as error:
    print(error)

# task2 - Поиск и удаление дубликатов
original_file = input('Введите имя файла: ')

def delete_dubs(file_name: str) -> None:
    """
    Удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.

    :param file_name: Имя оригинального файла в виде строки.
    """
    new_file_name = f'unique_{file_name}'
    lines_without_dubs = []
    with open(file_name, "r", encoding="utf-8") as origin_file, open(new_file_name, "w", encoding="utf-8") as new_file:
        for line in origin_file:
            if line not in lines_without_dubs:
                lines_without_dubs.append(line)
                new_file.write(line)

try:
    if not os.path.isfile(original_file):
        print('Ошибка: файл не существует.')
    else:
        delete_dubs(original_file)
        print(f'Дубликаты удалены. Уникальные строки сохранены в unique_{original_file}.')
except PermissionError as error:
    print(error)
except UnicodeDecodeError as error:
    print(error)
except OSError as error:
    print(error)
