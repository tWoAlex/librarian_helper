from sqlite3 import IntegrityError

from cruds.rent import RentCRUD

from . import MenuItem, get_date_menu, selection_menu
from .book_menu import Menu as BookMenu
from .client_menu import Menu as ClientMenu


class Menu:
    @staticmethod
    def create_menu():
        book, client, date = None, None, None
        data_collected = False
        while not data_collected:
            if book is None:
                book = BookMenu.get_by_id_menu()
            elif client is None:
                client = ClientMenu.get_by_id_menu()
            elif date is None:
                date = get_date_menu('Дата выдачи')
            else:
                data_collected = True
        try:
            RentCRUD.create(book_id=book[0], client_id=client[0], date=date)
        except IntegrityError as exc:
            print('\nНе удалось выдать книгу. '
                  f'База данных сообщила:\n"{exc.args[0]}"')

    @staticmethod
    def close_menu():
        client, book = None, None
        data_collected = False
        while not data_collected:
            if book is None:
                book = BookMenu.get_by_id_menu()
            elif client is None:
                client = ClientMenu.get_by_id_menu()
            else:
                data_collected = True
        rent = RentCRUD.get_by_client_and_book(
            client_id=client[0], book_id=book[0]
        )
        if rent is None:
            print('Актуальной записи о выдаче '
                  'этой книги этому читателю не найдена')
        else:
            print(rent)
            RentCRUD.close(id=rent[0])

    @staticmethod
    def retrieve_actual():
        print(*[
            '\nВыданные книги:',
            *[f'{author}, "{book}", {client}, {date}'
              for author, book, client, date
              in RentCRUD.get_all_actual()]
        ], sep='\n')


def rent_menu():
    menu_items = {
        '1': MenuItem('1. Список книг у читателей', Menu.retrieve_actual),
        '2': MenuItem('2. Выдать книгу в аренду', Menu.create_menu),
        '3': MenuItem('3. Принять книгу от читателя', Menu.close_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
