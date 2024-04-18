from cruds.author import author_crud

from . import MenuItem, get_number_menu, get_text_menu, selection_menu


class Menu:
    def all_menu(self):
        print(*[
            '\nАвторы:',
            *[f'{name} ({id})' for id, name in author_crud.get_all()]
        ], sep='\n')

    def get_by_id_menu(self) -> tuple[int, str]:
        author = None
        while author is None:
            id = get_number_menu('Номер автора')
            author = author_crud.get_by_id(id)
            if author is None:
                print('Автор в базе не найден')
        return author

    def create_menu(self) -> None:
        author_crud.create(get_text_menu('Имя автора'))

    def update_menu(self) -> None:
        author, name = None, None
        while any((author is None, name is None)):
            if author is None:
                author = self.get_by_id_menu()
            elif name is None:
                name = get_text_menu('Имя автора')
        author_crud.update(id=author[0], name=name)

    def delete_menu(self):
        author = None
        while author is None:
            author = self.get_by_id_menu()
        author_crud.delete(author[0])


menu = Menu()


def author_menu():
    menu_items = {
        '1': MenuItem('1. Список всех авторов (Автор, номер)',
                      menu.all_menu),
        '2': MenuItem('2. Создать автора', menu.create_menu),
        '3': MenuItem('3. Изменить автора', menu.update_menu),
        '4': MenuItem('4. Удалить автора', menu.delete_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
