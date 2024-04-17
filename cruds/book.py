from pathlib import Path

from db_connection import get_script_from_file, sql_execute

SCRIPTS_DIR = Path('sql').joinpath('book')
CREATE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('create.sql'))
DELETE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('delete.sql'))
UPDATE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('update.sql'))
GET_BY_ID_SCRIPT = get_script_from_file(
    SCRIPTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('retrieve_all.sql'))


class BookCRUD:
    @staticmethod
    def create(title: str, author_id: int,
               genre_id: int, quantity: int) -> None:
        sql_execute(CREATE_SCRIPT.format(title=title,
                                         author_id=author_id,
                                         genre_id=genre_id,
                                         quantity=quantity))

    @staticmethod
    def update(id: int, title: str, author_id: int, genre_id: int) -> None:
        sql_execute(UPDATE_SCRIPT.format(id=id,
                                         title=title,
                                         author_id=author_id,
                                         genre_id=genre_id))

    @staticmethod
    def delete(id: int) -> None:
        sql_execute(DELETE_SCRIPT.format(id=id))

    @staticmethod
    def get_by_id(id: int) -> int | None:
        books = sql_execute(GET_BY_ID_SCRIPT.format(id=id))
        if len(books):
            return books[0]

    @staticmethod
    def get_all() -> list[tuple[int, str, str, str]]:
        books = sql_execute(GET_ALL_SCRIPT)
        return books
