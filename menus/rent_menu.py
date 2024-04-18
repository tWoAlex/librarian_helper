from sqlite3 import IntegrityError

from cruds.rent import rent_crud

from . import MenuItem, get_date_menu, selection_menu
from .book_menu import menu as book_menu
from .client_menu import menu as client_menu


class Menu:
    def create_menu(self):
        book, client = None, None
        open_date, expected_close_date = None, None,
        data_collected = False
        while not data_collected:
            if book is None:
                book = book_menu.get_by_id_menu()
            elif client is None:
                client = client_menu.get_by_id_menu()
            elif open_date is None:
                open_date = get_date_menu('Дата выдачи')
            elif expected_close_date is None:
                expected_close_date = get_date_menu('Ожидаемая дата приёма')
            elif expected_close_date < open_date:
                print('Дата приёма меньше даты выдачи')
                open_date, expected_close_date = None, None
            else:
                data_collected = True
        try:
            rent_crud.create(
                book_id=book[0], client_id=client[0],
                open_date=open_date, expected_close_date=expected_close_date
            )
        except IntegrityError as exc:
            print('\nНе удалось выдать книгу. '
                  f'База данных сообщила:\n"{exc.args[0]}"')

    def close_menu(self):
        client, book, fact_close_date = None, None, None
        data_collected = False
        while not data_collected:
            if book is None:
                book = book_menu.get_by_id_menu()
            elif client is None:
                client = client_menu.get_by_id_menu()
            elif fact_close_date is None:
                fact_close_date = get_date_menu('Дата сдачи')
            else:
                data_collected = True
        rent = rent_crud.get_by_client_and_book(
            client_id=client[0], book_id=book[0]
        )
        if rent is None:
            print('Актуальной записи о выдаче '
                  'этой книги этому читателю не найдена')
        while fact_close_date is None:
            fact_close_date = get_date_menu('Дата сдачи')
        else:
            rent_crud.close(id=rent[0], fact_close_date=fact_close_date)

    def retrieve_actual(self):
        print(*[
            '\nВыданные книги:',
            *[f'{author}, "{book}", {client}, {open_date}'
              for author, book, client, open_date
              in rent_crud.get_all_actual()]
        ], sep='\n')


menu = Menu()


def rent_menu():
    menu_items = {
        '1': MenuItem('1. Список книг у читателей', menu.retrieve_actual),
        '2': MenuItem('2. Выдать книгу в аренду', menu.create_menu),
        '3': MenuItem('3. Принять книгу от читателя', menu.close_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
