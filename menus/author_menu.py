from cruds.author import AuthorCRUD

from . import MenuItem, get_number_menu, get_text_menu, selection_menu


class Menu:
    @staticmethod
    def all_menu():
        print(*[
            '\nАвторы:',
            *[f'{name} ({id})' for id, name in AuthorCRUD.get_all()]
        ], sep='\n')

    @staticmethod
    def get_by_id_menu() -> tuple[int, str]:
        author = None
        while author is None:
            id = get_number_menu('Номер автора')
            author = AuthorCRUD.get_by_id(id)
            if author is None:
                print('Автор в базе не найден')
        return author

    @staticmethod
    def create_menu() -> None:
        AuthorCRUD.create(get_text_menu('Имя автора'))

    @staticmethod
    def update_menu() -> None:
        author, name = None, None
        while any((author is None, name is None)):
            if author is None:
                author = Menu.get_by_id_menu()
            elif name is None:
                name = get_text_menu('Имя автора')
        AuthorCRUD.update(id=author[0], name=name)

    @staticmethod
    def delete_menu():
        author = None
        while author is None:
            author = Menu.get_by_id_menu()
        AuthorCRUD.delete(author[0])


def author_menu():
    menu_items = {
        '1': MenuItem('1. Список всех авторов (Автор, номер)',
                      Menu.all_menu),
        '2': MenuItem('2. Создать автора', Menu.create_menu),
        '3': MenuItem('3. Изменить автора', Menu.update_menu),
        '4': MenuItem('4. Удалить автора', Menu.delete_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
