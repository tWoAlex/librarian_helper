from pathlib import Path

from cruds.genre import GenreCRUD

from . import MenuItem, get_number_menu, get_text_menu, selection_menu


class Menu:
    @staticmethod
    def all_menu():
        print(*[
            '\nЖанры:',
            *[f'{title} ({id})' for id, title in GenreCRUD.get_all()]
        ], sep='\n')

    @staticmethod
    def get_by_id_menu() -> tuple[int, str]:
        genre = None
        while genre is None:
            id = get_number_menu('Номер жанра')
            genre = GenreCRUD.get_by_id(id)
            if genre is None:
                print('Жанр в базе не найден')
        return genre

    @staticmethod
    def create_menu() -> None:
        GenreCRUD.create(get_text_menu('Название жанра'))

    @staticmethod
    def update_menu() -> None:
        genre, title = None, None
        while any((genre is None, title is None)):
            if genre is None:
                genre = Menu.get_by_id_menu()
            elif title is None:
                title = Menu.get_title_menu()
        GenreCRUD.update(id=genre[0], title=title)

    @staticmethod
    def delete_menu():
        genre = None
        while genre is None:
            genre = Menu.get_by_id_menu()
        GenreCRUD.delete(genre[0])


def genre_menu():
    menu_items = {
        '1': MenuItem('1. Список всех жанров (жанр, номер)', Menu.all_menu),
        '2': MenuItem('2. Создать жанр', Menu.create_menu),
        '3': MenuItem('3. Изменить жанр', Menu.update_menu),
        '4': MenuItem('4. Удалить жанр', Menu.delete_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
