from cruds.book import BookCRUD

from . import MenuItem, get_number_menu, get_text_menu, selection_menu
from .author_menu import Menu as AuthorMenu
from .genre_menu import Menu as GenreMenu


class Menu:
    @staticmethod
    def all_menu():
        print(*[
            '\nКниги:',
            *[f'{id}. {author}. {title}. {genre} ({quantity})'
              for id, title, author, genre, quantity in BookCRUD.get_all()]
        ], sep='\n')

    @staticmethod
    def get_by_id_menu() -> tuple[int, str]:
        book = None

        def get_book():
            nonlocal book
            book = BookCRUD.get_by_id(get_number_menu('Номер книги'))

        get_book()
        while book is None:
            print('Книга в базе не найдена')
            get_book()
        return book

    @staticmethod
    def create_menu() -> None:
        title, author, genre, quantity = None, None, None, None
        data_collected = False
        while not data_collected:
            if title is None:
                title = get_text_menu('Название книги')
            elif author is None:
                author = AuthorMenu.get_by_id_menu()
            elif genre is None:
                genre = GenreMenu.get_by_id_menu()
            elif quantity is None:
                quantity = get_number_menu('Количество книг на балансе')
            else:
                data_collected = True
        BookCRUD.create(title=title, author_id=author[0],
                        genre_id=genre[0], quantity=quantity)

    @staticmethod
    def update_menu() -> None:
        book = Menu.get_by_id_menu()
        title, author, genre = None, None, None
        data_collected = False
        while not data_collected:
            if title is None:
                title = get_text_menu('Название')
            elif author is None:
                author = AuthorMenu.get_by_id_menu()
            elif genre is None:
                genre = GenreMenu.get_by_id_menu()
            else:
                data_collected = True
        BookCRUD.update(id=book[0], title=title,
                        author_id=author[0], genre_id=genre[0])

    @staticmethod
    def delete_menu():
        book = None
        while book is None:
            book = Menu.get_by_id_menu()
        BookCRUD.delete(book[0])


def book_menu() -> None:
    menu_items = {
        '1': MenuItem('1. Список всех книг', Menu.all_menu),
        '2': MenuItem('2. Добавить книгу', Menu.create_menu),
        '3': MenuItem('3. Изменить книгу', Menu.update_menu),
        '4': MenuItem('4. Удалить книгу', Menu.delete_menu),
        '0': MenuItem('0. Вернуться', None)
    }
    selection_menu(menu_items)
