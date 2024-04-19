from db_connection import SQL_REQUESTS_DIR, script_from_file, sql_execute

REPORTS_REQUESTS_DIR = SQL_REQUESTS_DIR.joinpath('reports')


class Reports:
    def books_how_many(self) -> int:
        """Возвращает общее количество книг на балансе библиотеки"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('books_how_many.sql')
        ))[0][0]

    def books_how_many_distinct(self) -> int:
        """Возвращает количество уникальных книг в библиотеке"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('books_how_many_distinct.sql')
        ))[0][0]

    def clients_how_many(self) -> int:
        """Возвращает количество зарегистрированных читателей"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_how_many.sql')
        ))[0][0]

    def clients_how_many_times(self) -> list[tuple[str, int]]:
        """Возвращает количество взятых каждым читателем книг за всё время
        в виде списка кортежей (имя_читателя, количество_книг)"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_how_many_times.sql')
        ))

    def clients_how_many_distinct_books(self) -> list[tuple[str, int]]:
        """Возвращает количество уникальных взятых каждым читателем книг
        за всё время в виде списка кортежей (имя_читателя, количество_книг)"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath(
                'clients_how_many_distinct_books.sql'
            )
        ))

    def clients_how_many_actual_rents(self) -> list[tuple[str, int]]:
        """Возвращает количество книг книг на руках у каждого читателя
        в виде списка кортежей (имя_читателя, количество_книг)"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_how_many_actual_rents.sql')
        ))

    def clients_last_visit(self) -> list[tuple[str, str]]:
        """Возвращает дату последнего визита каждого читателя
        в виде списка кортежей (имя_читателя, дата)"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_last_visit.sql')
        ))

    def author_most_popular(self) -> tuple[str, int]:
        """Возвращает данные о самом популярном авторе
        в виде кортежа (имя_автора, количество_уникальных_книг)"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('author_most_popular.sql')
        ))[0]

    def genres_most_popular(self) -> list[tuple[str, int]]:
        """Возвращает список жанров от самых популярных к наименее популярным
        в виде списка кортежей
        (название_жанра, количество_уникальных_взятий_книг)"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('genres_most_popular.sql')
        ))

    def clients_favorite_genre(self) -> list[tuple[str, int]]:
        """Возвращает данные о самых популярных жанрах для каждого читателя
        в виде списка кортежей
        (имя_читателя, название_жанра, количество_прочитанных_книг)"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('clients_favorite_genre.sql')
        ))

    def rents_expired(self) -> list[tuple[str, str, str, str]]:
        """Возвращает данные о просроченных, не осуществлённых возвратах
        в виде списка кортежей
        (имя_читателя, имя_автора, название_книги, ожидаемая_дата_сдачи)"""
        return sql_execute(script_from_file(
            REPORTS_REQUESTS_DIR.joinpath('rents_expired.sql')
        ))


reports = Reports()
