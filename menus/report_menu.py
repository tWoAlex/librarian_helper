from . import MenuItem, selection_menu

from cruds.report import Reports


class Menu:
    @staticmethod
    def books_how_many():
        print(f'В библиотеке {Reports.books_how_many()} книг')

    @staticmethod
    def books_how_many_distinct():
        print(f'В библиотеке {Reports.books_how_many_distinct()}'
              ' уникальных книг')

    @staticmethod
    def clients_how_many():
        print(f'У библиотеки {Reports.clients_how_many()} читателей')

    @staticmethod
    def clients_how_many_times():
        print(*[
            '\nЧитатели брали книги (раз):',
            *[f'{client}: {times}' for client, times
              in Reports.clients_how_many_times()]
        ], sep='\n')

    @staticmethod
    def clients_how_many_distinct_books():
        print(*[
            '\nЧитатели брали уникальных книг (раз):',
            *[f'{client}: {times}' for client, times
              in Reports.clients_how_many_distinct_books()]
        ], sep='\n')

    @staticmethod
    def clients_how_many_actual_rents():
        print(*[
            '\nКниг на руках у читателей:',
            *[f'{client}: {times}' for client, times
              in Reports.clients_how_many_actual_rents()]
        ], sep='\n')

    @staticmethod
    def clients_last_visit():
        print(*[
            *[f'{client}: {date}' for client, date
              in Reports.clients_last_visit()]
        ], sep='\n')

    @staticmethod
    def author_most_popular():
        name, count = Reports.author_most_popular()
        print(f'Самый популярный автор:\n'
              f'{name} ({count} уникальных читателей произведений)')

    @staticmethod
    def genres_most_popular():
        print(*[
            '\nПопулярность жанров:',
            *[f'{genre} ({count})' for genre, count
              in Reports.genres_most_popular()]
        ], sep='\n')

    @staticmethod
    def clients_favorite_genre():
        print(*[
            '\nСамые популярные жанры у клиентов:',
            *[f'{client}: {genre} ({count})'
              for client, genre, count in Reports.clients_favorite_genre()]
        ], sep='\n')


def report_menu():
    menu_items = {
        '1': MenuItem('1. Книги: сколько всего', Menu.books_how_many),
        '2': MenuItem('2. Книги: сколько уникальных',
                      Menu.books_how_many_distinct),
        '3': MenuItem('3. Читатели: сколько всего', Menu.clients_how_many),
        '4': MenuItem('4. Читатели: сколько раз брали книги',
                      Menu.clients_how_many_times),
        '5': MenuItem('5. Читатели: сколько брали уникальных книг',
                      Menu.clients_how_many_distinct_books),
        '6': MenuItem('6. Читатели: сколько книг на руках',
                      Menu.clients_how_many_actual_rents),
        '7': MenuItem('7. Читатели: дата последнего посещения',
                      Menu.clients_last_visit),
        '8': MenuItem('8. Самый популярный автор',
                      Menu.author_most_popular),
        '9': MenuItem('9. Жанры: популярность', Menu.genres_most_popular),
        '10': MenuItem('10. Жанры: самые популярные для читателей',
                       Menu.clients_favorite_genre),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
