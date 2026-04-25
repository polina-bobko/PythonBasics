# task1 - Анализ курсов студентов
import json
from datetime import datetime
from collections import defaultdict

DATE_FORMAT = "%d.%m.%Y"

def calculate_age(birth_date: str, enrollment_date: str) -> float:
    """
    Вычисляет возраст студента на момент поступления.

    Args:
        birth_date (str): дата рождения в формате 'дд.мм.гггг'
        enrollment_date (str): дата поступления в формате 'дд.мм.гггг'

    Returns:
        float: возраст на момент поступления (в полных годах)
    """
    birth = datetime.strptime(birth_date, DATE_FORMAT)
    enroll = datetime.strptime(enrollment_date, DATE_FORMAT)

    age = enroll.year - birth.year

    if (enroll.month, enroll.day) < (birth.month, birth.day):
        age -= 1
    return age


def analyze_students(data: list[dict]) -> dict:
    """
    Анализирует список студентов и формирует статистический отчёт.

    Args:
        data (list[dict]): список студентов с полями:
            - name (str)
            - birth_date (str)
            - enrollment_date (str)
            - courses (list[str])

    Returns:
        dict: отчёт, содержащий:
            - total_students (int)
            - average_enrollment_age (float)
            - students_per_course (dict)
    """
    total_students = len(data)
    total_age = 0
    course_counter = defaultdict(int)

    for student in data:
        age = calculate_age(
            student["birth_date"],
            student["enrollment_date"]
        )
        total_age += age

        for course in student["courses"]:
            course_counter[course] += 1

    average_age = round(total_age / total_students, 1)

    return {
        "total_students": total_students,
        "average_enrollment_age": average_age,
        "students_per_course": dict(sorted(course_counter.items()))
    }

with open("student_courses.json", "r", encoding="utf-8") as f:
    data = json.load(f)

report = analyze_students(data)

with open("student_courses_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=4)