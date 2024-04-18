from db_connection import script_from_file, sql_execute, SQL_REQUESTS_DIR

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('book')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
DELETE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('delete.sql'))
UPDATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('update.sql'))
GET_BY_ID_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_REQUEST = script_from_file(REQUESTS_DIR.joinpath('retrieve_all.sql'))


class BookCRUD:
    @staticmethod
    def create(title: str, author_id: int,
               genre_id: int, quantity: int) -> None:
        sql_execute(CREATE_REQUEST.format(title=title,
                                         author_id=author_id,
                                         genre_id=genre_id,
                                         quantity=quantity))

    @staticmethod
    def update(id: int, title: str, author_id: int, genre_id: int) -> None:
        sql_execute(UPDATE_REQUEST.format(id=id,
                                         title=title,
                                         author_id=author_id,
                                         genre_id=genre_id))

    @staticmethod
    def delete(id: int) -> None:
        sql_execute(DELETE_REQUEST.format(id=id))

    @staticmethod
    def get_by_id(id: int) -> int | None:
        books = sql_execute(GET_BY_ID_REQUEST.format(id=id))
        if len(books):
            return books[0]

    @staticmethod
    def get_all() -> list[tuple[int, str, str, str]]:
        books = sql_execute(GET_ALL_REQUEST)
        return books
