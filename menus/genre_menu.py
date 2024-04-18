from cruds.genre import genre_crud

from . import MenuItem, get_number_menu, get_text_menu, selection_menu


class Menu:
    def all_menu(self):
        print(*[
            '\nЖанры:',
            *[f'{title} ({id})' for id, title in genre_crud.get_all()]
        ], sep='\n')

    def get_by_id_menu(self) -> tuple[int, str]:
        genre = None
        while genre is None:
            id = get_number_menu('Номер жанра')
            genre = genre_crud.get_by_id(id)
            if genre is None:
                print('Жанр в базе не найден')
        return genre

    def create_menu(self) -> None:
        genre_crud.create(get_text_menu('Название жанра'))

    def update_menu(self) -> None:
        genre, title = None, None
        while any((genre is None, title is None)):
            if genre is None:
                genre = self.get_by_id_menu()
            elif title is None:
                title = get_text_menu('Название жанра')
        genre_crud.update(id=genre[0], title=title)

    def delete_menu(self):
        genre = None
        while genre is None:
            genre = self.get_by_id_menu()
        genre_crud.delete(genre[0])


menu = Menu()


def genre_menu():
    menu_items = {
        '1': MenuItem('1. Список всех жанров (жанр, номер)', menu.all_menu),
        '2': MenuItem('2. Создать жанр', menu.create_menu),
        '3': MenuItem('3. Изменить жанр', menu.update_menu),
        '4': MenuItem('4. Удалить жанр', menu.delete_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
