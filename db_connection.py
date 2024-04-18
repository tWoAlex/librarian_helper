import sqlite3
from pathlib import Path

DATABASE_FILE = Path('database.db')

SQL_REQUESTS_DIR = Path('sql')
DB_STRUCTURE_REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('create_db_structure')
DB_FULFILL_REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('fulfill_db')


def script_from_file(path: Path) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def sql_execute(script: str) -> list[tuple]:
    # Подключение к базе перенесено в метод, чтобы
    # обеспечить возможность удаления файла БД SQLite
    connection = sqlite3.connect(DATABASE_FILE)
    result = connection.execute(script)
    connection.commit()
    result = result.fetchall()
    connection.close()
    return result


def purge_db():
    Path(DATABASE_FILE).unlink(missing_ok=True)


def create_db():
    for script_file in Path(DB_STRUCTURE_REQUESTS_DIR).glob('*.sql'):
        sql_execute(script_from_file(script_file))


def fulfill_db():
    for script_file in Path(DB_FULFILL_REQUESTS_DIR).glob('*.sql'):
        sql_execute(script_from_file(script_file))
