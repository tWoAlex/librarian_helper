from db_connection import create_db, fulfill_db, purge_db

from . import MenuItem, selection_menu


def db_menu():
    menu_items = {
        '1': MenuItem('1. Создать базу', create_db),
        '2': MenuItem('2. Наполнить тестовыми данными', fulfill_db),
        '3': MenuItem('3. Снести базу', purge_db),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
