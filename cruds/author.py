from db_connection import SQL_REQUESTS_DIR, script_from_file, sql_execute

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('author')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
DELETE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('delete.sql'))
UPDATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('update.sql'))
GET_BY_ID_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_REQUEST = script_from_file(REQUESTS_DIR.joinpath('retrieve_all.sql'))


class AuthorCRUD:
    @staticmethod
    def create(name: str) -> None:
        sql_execute(CREATE_REQUEST.format(name=name))

    @staticmethod
    def update(id: int, name: str) -> None:
        sql_execute(UPDATE_REQUEST.format(id=id, name=name))

    @staticmethod
    def delete(id: int) -> None:
        sql_execute(DELETE_REQUEST.format(id=id))

    @staticmethod
    def get_by_id(id: int) -> int | None:
        authors = sql_execute(GET_BY_ID_REQUEST.format(id=id))
        if len(authors):
            return authors[0]

    @staticmethod
    def get_all() -> list[tuple[int, str]]:
        authors = sql_execute(GET_ALL_REQUEST)
        return sorted(authors, key=lambda x: x[1])
