from cruds.client import ClientCRUD

from . import ExitFromMenu, MenuItem, get_number_menu, selection_menu


class Menu:
    @staticmethod
    def all_menu():
        print(*[
            '\nЧитатели:',
            *[f'{name} ({id})' for id, name in ClientCRUD.get_all()]
        ], sep='\n')

    @staticmethod
    def get_by_id_menu() -> tuple[int, str]:
        client = None
        while client is None:
            id = get_number_menu('Номер читателя')
            client = ClientCRUD.get_by_id(id)
            if client is None:
                print('Читатель в базе не найден')
        return client

    @staticmethod
    def get_menu() -> str:
        name = input('Укажите имя читателя ("-" для выхода): ')
        if name == '-':
            raise ExitFromMenu()
        return name

    @staticmethod
    def create_menu() -> None:
        ClientCRUD.create(Menu.get_menu())

    @staticmethod
    def update_menu() -> None:
        client, name = None, None
        while any((client is None, name is None)):
            if client is None:
                client = Menu.get_by_id_menu()
            elif name is None:
                name = Menu.get_menu()
        ClientCRUD.update(id=client[0], name=name)

    @staticmethod
    def delete_menu():
        client = None
        while client is None:
            client = Menu.get_by_id_menu()
        ClientCRUD.delete(client[0])


def client_menu():
    menu_items = {
        '1': MenuItem('1. Список всех читателей (Автор, номер)',
                      Menu.all_menu),
        '2': MenuItem('2. Создать читателя', Menu.create_menu),
        '3': MenuItem('3. Изменить читателя', Menu.update_menu),
        '4': MenuItem('4. Удалить читателя', Menu.delete_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
