from db_connection import SQL_REQUESTS_DIR, script_from_file, sql_execute

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('genre')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
DELETE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('delete.sql'))
UPDATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('update.sql'))
GET_BY_ID_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_REQUEST = script_from_file(REQUESTS_DIR.joinpath('retrieve_all.sql'))


class GenreCRUD:
    def create(self, title: str) -> None:
        """Создаёт жанр с указанным названием"""
        sql_execute(CREATE_REQUEST.format(title=title))

    def update(self, id: int, title: str) -> None:
        """Обновляет название жанра с указанным ID"""
        sql_execute(UPDATE_REQUEST.format(id=id, title=title))

    def delete(self, id: int) -> None:
        """Удаляет жанр с указанным ID"""
        sql_execute(DELETE_REQUEST.format(id=id))

    def get_by_id(self, id: int) -> tuple[int, str] | None:
        """Возвращает данные о жанре с указанным ID
        в виде кортежа (id, название_жанра)"""
        genres = sql_execute(GET_BY_ID_REQUEST.format(id=id))
        if len(genres):
            return genres[0]

    def get_all(self) -> list[tuple[int, str]]:
        """Возвращает список жанров в виде кортежей (id, название_жанра)"""
        genres = sql_execute(GET_ALL_REQUEST)
        return sorted(genres, key=lambda x: x[1])


genre_crud = GenreCRUD()
