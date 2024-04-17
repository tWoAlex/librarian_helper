from pathlib import Path

from db_connection import get_script_from_file, sql_execute

SCRIPTS_DIR = Path('sql').joinpath('genre')
CREATE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('create.sql'))
CREATE_MULTIPLE_SCRIPT = get_script_from_file(
    SCRIPTS_DIR.joinpath('create_multiple.sql'))
DELETE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('delete.sql'))
UPDATE_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('update.sql'))
GET_BY_ID_SCRIPT = get_script_from_file(
    SCRIPTS_DIR.joinpath('retrieve_by_id.sql'))
GET_ALL_SCRIPT = get_script_from_file(SCRIPTS_DIR.joinpath('retrieve_all.sql'))


class GenreCRUD:
    @staticmethod
    def create(title: str) -> None:
        sql_execute(CREATE_SCRIPT.format(title=title))

    @staticmethod
    def create_multiple(titles: list[str]) -> None:
        sql_execute(CREATE_MULTIPLE_SCRIPT.format(
            values=',\n'.join(
                [f'("{title}")' for title in titles]
            )
        ))

    @staticmethod
    def update(id: int, title: str) -> None:
        sql_execute(UPDATE_SCRIPT.format(id=id, title=title))

    @staticmethod
    def delete(id: int) -> None:
        sql_execute(DELETE_SCRIPT.format(id=id))

    @staticmethod
    def get_by_id(id: int) -> int | None:
        genres = sql_execute(GET_BY_ID_SCRIPT.format(id=id))
        if len(genres):
            return genres[0]

    @staticmethod
    def get_all() -> list[tuple[int, str]]:
        genres = sql_execute(GET_ALL_SCRIPT)
        return sorted(genres, key=lambda x: x[1])
