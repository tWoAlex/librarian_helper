from db_connection import script_from_file, sql_execute, SQL_REQUESTS_DIR

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('genre')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
DELETE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('delete.sql'))
UPDATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('update.sql'))
GET_BY_ID_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_REQUEST = script_from_file(REQUESTS_DIR.joinpath('retrieve_all.sql'))


class GenreCRUD:
    @staticmethod
    def create(title: str) -> None:
        sql_execute(CREATE_REQUEST.format(title=title))

    @staticmethod
    def update(id: int, title: str) -> None:
        sql_execute(UPDATE_REQUEST.format(id=id, title=title))

    @staticmethod
    def delete(id: int) -> None:
        sql_execute(DELETE_REQUEST.format(id=id))

    @staticmethod
    def get_by_id(id: int) -> int | None:
        genres = sql_execute(GET_BY_ID_REQUEST.format(id=id))
        if len(genres):
            return genres[0]

    @staticmethod
    def get_all() -> list[tuple[int, str]]:
        genres = sql_execute(GET_ALL_REQUEST)
        return sorted(genres, key=lambda x: x[1])
