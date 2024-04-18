from cruds.book import book_crud

from . import MenuItem, get_number_menu, get_text_menu, selection_menu
from .author_menu import menu as author_menu
from .genre_menu import menu as genre_menu


class Menu:
    def all_menu(self):
        print(*[
            '\nКниги:',
            *[f'{id}. {author}, "{title}". {genre} ({quantity})'
              for id, title, author, genre, quantity in book_crud.get_all()]
        ], sep='\n')

    def get_by_id_menu(self) -> tuple[int, str]:
        book = None

        def get_book():
            nonlocal book
            book = book_crud.get_by_id(get_number_menu('Номер книги'))

        get_book()
        while book is None:
            print('Книга в базе не найдена')
            get_book()
        return book

    def create_menu(self) -> None:
        title, author, genre, quantity = None, None, None, None
        data_collected = False
        while not data_collected:
            if title is None:
                title = get_text_menu('Название книги')
            elif author is None:
                author = author_menu.get_by_id_menu()
            elif genre is None:
                genre = genre_menu.get_by_id_menu()
            elif quantity is None:
                quantity = get_number_menu('Количество книг на балансе')
            else:
                data_collected = True
        book_crud.create(title=title, author_id=author[0],
                         genre_id=genre[0], quantity=quantity)

    def update_menu(self) -> None:
        book = Menu.get_by_id_menu()
        title, author, genre = None, None, None
        data_collected = False
        while not data_collected:
            if title is None:
                title = get_text_menu('Название')
            elif author is None:
                author = author_menu.get_by_id_menu()
            elif genre is None:
                genre = genre_menu.get_by_id_menu()
            else:
                data_collected = True
        book_crud.update(id=book[0], title=title,
                         author_id=author[0], genre_id=genre[0])

    def delete_menu(self):
        book = None
        while book is None:
            book = self.get_by_id_menu()
        book_crud.delete(book[0])


menu = Menu()


def book_menu() -> None:
    menu_items = {
        '1': MenuItem('1. Список всех книг', menu.all_menu),
        '2': MenuItem('2. Добавить книгу', menu.create_menu),
        '3': MenuItem('3. Изменить книгу', menu.update_menu),
        '4': MenuItem('4. Удалить книгу', menu.delete_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
