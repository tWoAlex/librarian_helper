from db_connection import SQL_REQUESTS_DIR, script_from_file, sql_execute

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('author')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
DELETE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('delete.sql'))
UPDATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('update.sql'))
GET_BY_ID_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_REQUEST = script_from_file(REQUESTS_DIR.joinpath('retrieve_all.sql'))


class AuthorCRUD:
    def create(self, name: str) -> None:
        """Создаёт автора с указанным именем"""
        sql_execute(CREATE_REQUEST.format(name=name))

    def update(self, id: int, name: str) -> None:
        """Обновляет имя автора с указанным ID"""
        sql_execute(UPDATE_REQUEST.format(id=id, name=name))

    def delete(self, id: int) -> None:
        """Удаляет автора с указанным ID"""
        sql_execute(DELETE_REQUEST.format(id=id))

    def get_by_id(self, id: int) -> tuple[int, str] | None:
        """Возвращает данные автора по ID
        в виде кортежа (id, имя_автора)"""
        authors = sql_execute(GET_BY_ID_REQUEST.format(id=id))
        if len(authors):
            return authors[0]

    def get_all(self) -> list[tuple[int, str]]:
        """Возвращает список авторов
        в виде кортежей (id, имя_автора)"""
        authors = sql_execute(GET_ALL_REQUEST)
        return sorted(authors, key=lambda x: x[1])


author_crud = AuthorCRUD()
