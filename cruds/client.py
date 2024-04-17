from pathlib import Path

from db_connection import get_script_from_file, sql_execute

SCRIPTS_DIR = Path('sql').joinpath('client')
CREATE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('create.sql'))
DELETE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('delete.sql'))
UPDATE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('update.sql'))
GET_BY_ID_SCRIPT = get_script_from_file(
    SCRIPTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('retrieve_all.sql'))


class ClientCRUD:
    @staticmethod
    def create(name: str) -> None:
        sql_execute(CREATE_SCRIPT.format(name=name))

    @staticmethod
    def update(id: int, name: str) -> None:
        sql_execute(UPDATE_SCRIPT.format(id=id, name=name))

    @staticmethod
    def delete(id: int) -> None:
        sql_execute(DELETE_SCRIPT.format(id=id))

    @staticmethod
    def get_by_id(id: int) -> int | None:
        clients = sql_execute(GET_BY_ID_SCRIPT.format(id=id))
        if len(clients):
            return clients[0]

    @staticmethod
    def get_all() -> list[tuple[int, str]]:
        clients = sql_execute(GET_ALL_SCRIPT)
        return sorted(clients, key=lambda x: x[1])
