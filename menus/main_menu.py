from . import ExitFromMenu, MenuItem, selection_menu
from .author_menu import author_menu
from .book_menu import book_menu
from .client_menu import client_menu
from .db_menu import db_menu
from .genre_menu import genre_menu
from .rent_menu import rent_menu
from .report_menu import report_menu


def main_menu():
    menu_items = {
        '1': MenuItem('1. Авторы', author_menu),
        '2': MenuItem('2. Жанры', genre_menu),
        '3': MenuItem('3. Книги', book_menu),
        '4': MenuItem('4. Читатели', client_menu),
        '5': MenuItem('5. Аренда книг', rent_menu),
        '6': MenuItem('6. Просмотр отчётов', report_menu),
        '9': MenuItem('9. Управление базой', db_menu),
        '0': MenuItem('0. Завершить работу', None)
    }
    try:
        selection_menu(menu_items)
    except ExitFromMenu:
        exit()
