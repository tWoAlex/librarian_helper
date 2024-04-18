from db_connection import sql_execute, SQL_REQUESTS_DIR, script_from_file


REPORTS_REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('reports')


class Reports:
    @staticmethod
    def books_how_many() -> int:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('books_how_many.sql')
        ))[0][0]

    @staticmethod
    def books_how_many_distinct() -> int:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('books_how_many_distinct.sql')
        ))[0][0]

    @staticmethod
    def clients_how_many() -> int:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_how_many.sql')
        ))[0][0]

    @staticmethod
    def clients_how_many_times() -> list[tuple[str, int]]:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_how_many_times.sql')
        ))

    @staticmethod
    def clients_how_many_distinct_books() -> list[tuple[str, int]]:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath(
                'clients_how_many_distinct_books.sql'
            )
        ))

    @staticmethod
    def clients_how_many_actual_rents() -> list[tuple[str, int]]:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_how_many_actual_rents.sql')
        ))

    @staticmethod
    def clients_last_visit() -> list[tuple[str, str]]:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_last_visit.sql')
        ))

    @staticmethod
    def author_most_popular() -> tuple[str, int]:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('author_most_popular.sql')
        ))[0]

    @staticmethod
    def genres_most_popular() -> list[tuple[str, int]]:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('genres_most_popular.sql')
        ))

    @staticmethod
    def clients_favorite_genre() -> list[tuple[str, int]]:
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_favorite_genre.sql')
        ))
