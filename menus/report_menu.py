from copy import deepcopy
from json import dumps

from cruds.report import reports

from . import MenuItem, selection_menu


class Menu:
    def books_how_many(self):
        print(f'В библиотеке {reports.books_how_many()} книг')

    def books_how_many_distinct(self):
        print(f'В библиотеке {reports.books_how_many_distinct()}'
              ' уникальных книг')

    def clients_how_many(self):
        print(f'У библиотеки {reports.clients_how_many()} читателей')

    def clients_how_many_times(self):
        print(*[
            '\nЧитатели брали книги (раз):',
            *[f'{client}: {times}' for client, times
              in reports.clients_how_many_times()]
        ], sep='\n')

    def clients_how_many_distinct_books(self):
        print(*[
            '\nЧитатели брали уникальных книг (раз):',
            *[f'{client}: {times}' for client, times
              in reports.clients_how_many_distinct_books()]
        ], sep='\n')

    def clients_how_many_actual_rents(self):
        print(*[
            '\nКниг на руках у читателей:',
            *[f'{client}: {times}' for client, times
              in reports.clients_how_many_actual_rents()]
        ], sep='\n')

    def clients_last_visit(self):
        print(*[
            *[f'{client}: {date}' for client, date
              in reports.clients_last_visit()]
        ], sep='\n')

    def author_most_popular(self):
        name, count = reports.author_most_popular()
        print(f'Самый популярный автор:\n'
              f'{name} ({count} уникальных читателей произведений)')

    def genres_most_popular(self):
        print(*[
            '\nПопулярность жанров:',
            *[f'{genre} ({count})' for genre, count
              in reports.genres_most_popular()]
        ], sep='\n')

    def clients_favorite_genre(self):
        print(*[
            '\nСамые популярные жанры у клиентов:',
            *[f'{client}: {genre} ({count})'
              for client, genre, count in reports.clients_favorite_genre()]
        ], sep='\n')

    def rents_expired(self):
        report_file = 'Просроченные возвраты.txt'
        with open(report_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join([
                'Просроченные возвраты:\n',
                *[f'{client}: {author}, "{book}" ({expected_date})'
                  for client, author, book, expected_date
                  in reports.rents_expired()]
            ]))
        print('Отчёт о просроченных возвратах размещён в файле '
              f'"{report_file}"')

    __GEORECORD = {
        'type': 'Feature',
        'geometry': {'type': 'Point', 'coordinates': None},
        'properties': {'author': None, 'book': None, 'client': None}
    }
    __GEODICT_MAIN = {'type': 'FeatureCollection',
                      'features': None}

    def __generate_georecord(author: str, book: str, client: str,
                             longitude: float, latitude: float) -> dict:
        new_record = deepcopy(Menu.__GEORECORD)
        new_record['geometry']['coordinates'] = [longitude, latitude]

        properties = new_record['properties']
        properties['author'] = author
        properties['book'] = book
        properties['client'] = client

        return new_record

    def __generate_geodict(
            rents: list[tuple[str, str, str, float, float]]) -> dict:
        geodict = deepcopy(Menu.__GEODICT_MAIN)
        geodict['features'] = [
            Menu.__generate_georecord(*rent) for rent in rents
        ]
        return geodict

    def rents_actual_with_coords(self):
        report_file = 'Actual_rents_with_coords.json'
        data = Menu.__generate_geodict(
            reports.rents_actual_with_coords()
        )
        with open(report_file, 'w', encoding='utf-8') as file:
            file.write(dumps(data, ensure_ascii=False))
        print('Отчёт об книгах на руках у пользователей размещён в файле '
              f'"{report_file}"')


menu = Menu()


def report_menu():
    menu_items = {
        '1': MenuItem('1. Книги: сколько всего', menu.books_how_many),
        '2': MenuItem('2. Книги: сколько уникальных',
                      menu.books_how_many_distinct),
        '3': MenuItem('3. Читатели: сколько всего', menu.clients_how_many),
        '4': MenuItem('4. Читатели: сколько раз брали книги',
                      menu.clients_how_many_times),
        '5': MenuItem('5. Читатели: сколько брали уникальных книг',
                      menu.clients_how_many_distinct_books),
        '6': MenuItem('6. Читатели: сколько книг на руках',
                      menu.clients_how_many_actual_rents),
        '7': MenuItem('7. Читатели: дата последнего посещения',
                      menu.clients_last_visit),
        '8': MenuItem('8. Самый популярный автор',
                      menu.author_most_popular),
        '9': MenuItem('9. Жанры: популярность', menu.genres_most_popular),
        '10': MenuItem('10. Жанры: самые популярные для читателей',
                       menu.clients_favorite_genre),
        '11': MenuItem('11. Просроченные возвраты', menu.rents_expired),
        '12': MenuItem('12. Книги у читателей с координатами',
                       menu.rents_actual_with_coords),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
