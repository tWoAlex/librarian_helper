from db_connection import SQL_REQUESTS_DIR, script_from_file, sql_execute

REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('client')
CREATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('create.sql'))
DELETE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('delete.sql'))
UPDATE_REQUEST = script_from_file(REQUESTS_DIR.joinpath('update.sql'))
GET_BY_ID_REQUEST = script_from_file(
    REQUESTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_REQUEST = script_from_file(REQUESTS_DIR.joinpath('retrieve_all.sql'))


class ClientCRUD:
    def create(self, name: str) -> None:
        """Создаёт читателя с указанным именем"""
        sql_execute(CREATE_REQUEST.format(name=name))

    def update(self, id: int, name: str) -> None:
        """Обновляет имя читателя с указанным ID"""
        sql_execute(UPDATE_REQUEST.format(id=id, name=name))

    def delete(self, id: int) -> None:
        """Удаляет читателя с указанным ID"""
        sql_execute(DELETE_REQUEST.format(id=id))

    def get_by_id(self, id: int) -> tuple[int, str] | None:
        """Возвращает данные читателя с указанным ID
        в виде кортежа (id, имя_читателя)"""
        clients = sql_execute(GET_BY_ID_REQUEST.format(id=id))
        if len(clients):
            return clients[0]

    def get_all(self) -> list[tuple[int, str]]:
        """Возвращает список читателей
        в виде кортежей (id, имя_читателя)"""
        clients = sql_execute(GET_ALL_REQUEST)
        return sorted(clients, key=lambda x: x[1])


client_crud = ClientCRUD()
