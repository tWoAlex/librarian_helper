from datetime import date
from pathlib import Path

from db_connection import get_script_from_file, sql_execute

SCRIPTS_DIR = Path('sql').joinpath('rent')
CREATE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('create.sql'))
GET_ACTUAL_SCRIPT = get_script_from_file(
    SCRIPTS_DIR.joinpath('retrieve_actual.sql'))
GET_BY_CLIENT_AND_BOOK_SCRIPT = get_script_from_file(
    SCRIPTS_DIR.joinpath('retrieve_by_client_and_book.sql'))
CLOSE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('close.sql'))


class RentCRUD:
    @staticmethod
    def create(book_id: int, client_id: int, date: date):
        sql_execute(CREATE_SCRIPT.format(
            book_id=book_id, client_id=client_id, date=str(date), closed=0
        ))

    @staticmethod
    def get_by_client_and_book(client_id: int, book_id: int) -> tuple | None:
        """Ищет запись о выдаче по данным читателя и книги"""
        results = sql_execute(GET_BY_CLIENT_AND_BOOK_SCRIPT.format(
            client_id=client_id, book_id=book_id
        ))
        if not len(results):
            return None
        return results[0]

    @staticmethod
    def close(id: int):
        sql_execute(CLOSE_SCRIPT.format(id=id))

    @staticmethod
    def get_all_actual():
        return sql_execute(GET_ACTUAL_SCRIPT)
