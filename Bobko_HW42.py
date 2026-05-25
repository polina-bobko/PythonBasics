# task 1 - Создание базы
# task 2 - Добавление заметок

import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env_edit')

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password')
}

db_name = "notes_app_121225ptm_PolinaBobko"

try:
    with pymysql.connect(**config) as conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            cursor.execute(f"USE {db_name}")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    content TEXT
                )
            """)
            #cursor.execute("DELETE FROM notes")
            #cursor.execute("ALTER TABLE notes AUTO_INCREMENT = 1")
            title = "Shopping list"
            content = "Milk, bread, eggs"
            cursor.execute(
                "INSERT INTO notes (title, content) VALUES (%s, %s)",
                (title, content)
            )
            conn.commit()
            print(f"Note added: {title}")

            cursor.execute("SELECT * FROM notes")

            notes = cursor.fetchall()

            for note in notes:
                print(f"{note['id']}. {note['title']} — {note['content']}")


except pymysql.MySQLError as e:
    print(f"MySQL error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")