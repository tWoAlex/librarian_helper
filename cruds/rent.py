from datetime import date

from db_connection import script_from_file, sql_execute, SQL_REQUESTS_DIR

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('rent')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
GET_ACTUAL_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_actual.sql'))
GET_BY_CLIENT_AND_BOOK_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_client_and_book.sql'))
CLOSE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('close.sql'))


class RentCRUD:
    @staticmethod
    def create(book_id: int, client_id: int, date: date):
        sql_execute(CREATE_REQUEST.format(
            book_id=book_id, client_id=client_id, date=str(date), closed=0
        ))

    @staticmethod
    def get_by_client_and_book(client_id: int, book_id: int) -> tuple | None:
        """Ищет запись о выдаче по данным читателя и книги"""
        results = sql_execute(GET_BY_CLIENT_AND_BOOK_REQUEST.format(
            client_id=client_id, book_id=book_id
        ))
        if not len(results):
            return None
        return results[0]

    @staticmethod
    def close(id: int):
        sql_execute(CLOSE_REQUEST.format(id=id))

    @staticmethod
    def get_all_actual():
        return sql_execute(GET_ACTUAL_REQUEST)
