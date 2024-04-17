import sqlite3
from pathlib import Path

DATABASE_FILE = Path('database.db')
DB_STRUCTURE_SCRIPTS_DIR = Path('sql').joinpath('create_db_structure')


def get_script_from_file(path: Path) -> str:
    with open(path, 'r') as file:
        return file.read()


def sql_execute(script: str) -> list[tuple]:
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    result = cursor.execute(script)
    connection.commit()
    result = result.fetchall()

    cursor.close()
    connection.close()
    return result


def purge_db():
    Path(DATABASE_FILE).unlink(missing_ok=True)


def create_db():
    for script_file in Path(DB_STRUCTURE_SCRIPTS_DIR).glob('*.sql'):
        sql_execute(get_script_from_file(script_file))
