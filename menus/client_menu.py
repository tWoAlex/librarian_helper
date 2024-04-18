from cruds.client import client_crud

from . import MenuItem, get_number_menu, get_text_menu, selection_menu


class Menu:
    def all_menu(self):
        print(*[
            '\nЧитатели:',
            *[f'{name} ({id})' for id, name in client_crud.get_all()]
        ], sep='\n')

    def get_by_id_menu(self) -> tuple[int, str]:
        client = None
        while client is None:
            id = get_number_menu('Номер читателя')
            client = client_crud.get_by_id(id)
            if client is None:
                print('Читатель в базе не найден')
        return client

    def create_menu(self) -> None:
        client_crud.create(get_text_menu('Имя читателя'))

    def update_menu(self) -> None:
        client, name = None, None
        while any((client is None, name is None)):
            if client is None:
                client = self.get_by_id_menu()
            elif name is None:
                name = get_text_menu('Имя читателя')
        client_crud.update(id=client[0], name=name)

    def delete_menu(self):
        client = None
        while client is None:
            client = self.get_by_id_menu()
        client_crud.delete(client[0])


menu = Menu()


def client_menu():
    menu_items = {
        '1': MenuItem('1. Список всех читателей (Автор, номер)',
                      menu.all_menu),
        '2': MenuItem('2. Создать читателя', menu.create_menu),
        '3': MenuItem('3. Изменить читателя', menu.update_menu),
        '4': MenuItem('4. Удалить читателя', menu.delete_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
