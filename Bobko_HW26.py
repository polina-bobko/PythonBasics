# task 1 - Список файлов и папок
import os
import sys

def get_directory_content(path: str) -> tuple[list[str], list[str]]:
    """
    Возвращает списки папок и файлов в указанной директории.

    :param path: Путь к директории, строка.
    :return: Кортеж, состоящий из двух списков - папки и файлы
    """
    folders = []
    files = []
    ignored = {".venv", ".git", ".idea", "__pycache__"}

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path) and item not in ignored:
            folders.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

    return folders, files

if len(sys.argv) != 2:
    print("Использование: python3 Bobko_HW26.py <директория>")
    sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"Директория '{directory}' не существует.")
    sys.exit(1)

folders, files = get_directory_content(directory)

print(f"\nСодержимое директории '{directory}':\n")

print("Папки:")
if folders:
    for folder in folders:
        print(f"- {folder}")
else:
    print("Пусто")

print("\nФайлы:")
if files:
    for file in files:
        print(f"- {file}")
else:
    print("Пусто")

# /Users/polina_bobko/PycharmProjects
# /Users/polina_bobko/PycharmProjects/PythonBasics

# task 2 - Поиск и удаление файлов с указанным расширением
import os
import sys

def get_files_by_extension(path: str, extension: str) -> list[str]:
    """
    Рекурсивно ищет файлы с указанным расширением.

    :param path: Директория для поиска.
    :param extension: Расширение файлов (например, .log).
    :return: Список найденных файлов.
    """
    found_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files

def delete_files(files: list[str]) -> list[str]:
    """
    Удаляет файлы и возвращает список тех, которые удалить не удалось.

    :param files: Список файлов для удаления.
    :return: Список файлов с ошибкой удаления.
    """
    failed_files = []
    for file in files:
        try:
            os.remove(file)
        except PermissionError:
            failed_files.append(file)
    return failed_files

if len(sys.argv) != 3:
    print("Использование: python3 Bobko_HW26.py <директория> <расширение>")
    sys.exit(1)

directory = sys.argv[1]
extension = sys.argv[2]

if not os.path.isdir(directory):
    print(f"Директория '{directory}' не существует.")
    sys.exit(1)

if not os.listdir(directory):
    print("Директория пуста.")
    sys.exit(0)

if not extension.startswith("."):
    print("Расширение должно начинаться с точки, например .log")
    sys.exit(1)

found_files = get_files_by_extension(directory, extension)

if found_files:
    print(f"\nНайдены файлы с расширением '{extension}':\n")
    for file in found_files:
        print(f"- {file}")
else:
    print(f"\nФайлы с расширением '{extension}' не найдены.")
    sys.exit(0)

confirm = input("\nВы хотите удалить эти файлы? (y/n): ").lower()

if confirm == "y":
    failed = delete_files(found_files)

    if failed:
        print("\nНе удалось удалить следующие файлы:")
        for file in failed:
            print(f"- {file}")
    else:
        print("Удаление завершено.")
else:
    print("Удаление отменено.")