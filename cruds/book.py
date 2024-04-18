from db_connection import SQL_REQUESTS_DIR, script_from_file, sql_execute

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('book')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
DELETE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('delete.sql'))
UPDATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('update.sql'))
GET_BY_ID_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_REQUEST = script_from_file(REQUESTS_DIR.joinpath('retrieve_all.sql'))


class BookCRUD:
    def create(self, title: str, author_id: int,
               genre_id: int, quantity: int) -> None:
        """Создаёт книгу с указанными параметрами"""
        sql_execute(CREATE_REQUEST.format(
            title=title, author_id=author_id,
            genre_id=genre_id, quantity=quantity))

    def update(self, id: int, title: str,
               author_id: int, genre_id: int) -> None:
        """Обновляет данные о книге с указанным ID"""
        sql_execute(UPDATE_REQUEST.format(
            id=id, title=title, author_id=author_id, genre_id=genre_id)
        )

    def delete(self, id: int) -> None:
        """Удаляет книгу с указанным ID"""
        sql_execute(DELETE_REQUEST.format(id=id))

    def get_by_id(self, id: int) -> tuple[int, int, int, str, int] | None:
        """Возвращает данные о книге с указанным ID
        в виде кортежа (id, id_автора, id_жанра,
         название, количество_на_балансе)"""
        books = sql_execute(GET_BY_ID_REQUEST.format(id=id))
        if len(books):
            return books[0]

    def get_all(self) -> list[tuple[int, str, str, str]]:
        """Возвращает данные обо всех книгах на балансе
        в виде списка кортежей (id, id_автора, id_жанра,
         название, количество_на_балансе)"""
        books = sql_execute(GET_ALL_REQUEST)
        return books


book_crud = BookCRUD()
