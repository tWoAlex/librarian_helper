from datetime import date

from db_connection import SQL_REQUESTS_DIR, script_from_file, sql_execute

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('rent')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
GET_ACTUAL_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_actual.sql'))
GET_BY_CLIENT_AND_BOOK_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_client_and_book.sql'))
CLOSE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('close.sql'))


class RentCRUD:
    def create(self,
               book_id: int, client_id: int,
               open_date: date, expected_close_date: date) -> None:
        """Создаёт запись о выдаче указанной книги
        с указанным читателем в указанную дату и с ожидаемой датой возврата"""
        sql_execute(CREATE_REQUEST.format(
            book_id=book_id, client_id=client_id,
            open_date=str(open_date),
            expected_close_date=str(expected_close_date)
        ))

    def get_by_client_and_book(
            self, client_id: int, book_id: int) -> tuple[int, str] | None:
        """Ищет запись о выдаче по данным читателя и книги
        в виде кортежа ()"""
        results = sql_execute(GET_BY_CLIENT_AND_BOOK_REQUEST.format(
            client_id=client_id, book_id=book_id
        ))
        if not len(results):
            return None
        return results[0]

    def close(self, id: int, fact_close_date: date) -> None:
        """Принимает у читателя книгу по записи с указанным ID
        в указанную дату"""
        sql_execute(CLOSE_REQUEST.format(
            id=id, fact_close_date=str(fact_close_date)
        ))

    def get_all_actual(self) -> list[tuple]:
        """Возвращает список записей о книгах, находящихся у читателей"""
        return sql_execute(GET_ACTUAL_REQUEST)


rent_crud = RentCRUD()
