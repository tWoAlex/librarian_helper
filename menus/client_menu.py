from cruds.client import client_crud

from . import (MenuItem,
               get_coord_float_menu, get_number_menu, get_text_menu,
               selection_menu)


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
        name, longitude, latitude = None, None, None
        data_collected = False
        while not data_collected:
            if name is None:
                name = get_text_menu('Имя читателя')
            elif longitude is None:
                longitude = get_coord_float_menu('Адрес, долгота')
            elif latitude is None:
                latitude = get_coord_float_menu('Адрес, широта')
            else:
                data_collected = True
        client_crud.create(
            name=name, longitude=longitude, latitude=latitude
        )

    def update_menu(self) -> None:
        client, name = None, None
        longitude, latitude = None, None
        data_collected = False
        while not data_collected:
            if client is None:
                client = self.get_by_id_menu()
            elif name is None:
                name = get_text_menu('Имя читателя')
            elif longitude is None:
                longitude = get_coord_float_menu('Адрес, долгота')
            elif latitude is None:
                latitude = get_coord_float_menu('Адрес, широта')
            else:
                data_collected = True
        client_crud.update(id=client[0], name=name,
                           longitude=longitude, latitude=latitude)

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
