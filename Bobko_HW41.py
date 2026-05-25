# task 1 - Список всех стран

import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_DATABASE', 'world'),
}

with pymysql.connect(**config) as conn:
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT Name FROM country ORDER BY Name')

        for num, row in enumerate(cursor, 1):
            print(f"{num}. {row['Name']}")

# task 2 - Города выбранной страны

import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_DATABASE', 'world'),
}

country_name = input("Введите страну: ").strip().lower()

with pymysql.connect(**config) as conn:
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(
            "SELECT Code FROM country WHERE LOWER(Name) = %s",
            (country_name,)
        )
        country = cursor.fetchone()

        if not country:
            print("Страна не найдена")
        else:
            country_code = country['Code']
            cursor.execute(
                """
                SELECT Name, Population
                FROM city
                WHERE CountryCode = %s
                ORDER BY Population DESC
                """,
                (country_code,)
            )

            cities = cursor.fetchall()

            if not cities:
                print("В этой стране нет городов")
            else:
                for num, city in enumerate(cities, 1):
                    print(f"{num}. {city['Name']} — {city['Population']}")