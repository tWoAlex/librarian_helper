import re
from datetime import date
from os import system
from typing import Any

DATE_REGEX = re.compile(r'(?P<day>\d{2}).(?P<month>\d{2}).(?P<year>\d{4})')


def clear_console():
    system('cls')


class MenuItem:
    def __init__(self, title, method) -> None:
        self.title = title
        self.method = method

    def __str__(self) -> str:
        return self.title

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.method()


class ExitFromMenu(StopIteration):
    """Класс исключений, вызываемых для прерывания текущего меню
    или цикла запроса данных у пользователя"""
    ...


# Стандартные меню запроса данных по типам:

def get_number_menu(question: str) -> int | str:
    """Запрашивает у пользователя неотрицательное число
    или знак \"-\" для выхода из меню."""
    count = None
    while count is None:
        count = input(f'{question} ("-" для выхода): ')
        if count == '-':
            raise ExitFromMenu()
        try:
            count = int(count)
            if count < 0:
                raise ValueError()
        except ValueError:
            count = None
            print('Введено некорректное число')
    return count


def get_number_or_empty_menu(question: str) -> int | str:
    """Запрашивает у пользователя неотрицательное число,
    пустую строку или знак \"-\" для выхода из меню.
    Пустая строка нужна сохранения текущего значения в контексте
    работы с ранее созданной сущностью"""

    count = None
    while count is None:
        count = input(
            f'{question} ("-" для выхода, Enter для сохранения текущего): '
        )
        if count == '-':
            raise ExitFromMenu()
        elif count == '':
            break
        try:
            count = int(count)
            if count < 0:
                raise ValueError()
        except ValueError:
            count = None
            print('Введено некорректное число')
    return count


def get_text_menu(question: str) -> str:
    """Запрашивает у пользователя непустое строковое значение
    или знак \"-\" для выхода из меню."""

    title = None
    while title is None:
        title = input(f'{question} ("-" для выхода): ')
        if not len(title):
            print('Введена пустая строка')
        if title == '-':
            raise ExitFromMenu()
    return title


def get_text_or_empty_menu(question: str) -> str:
    """Запрашивает у пользователя строковое значение
    или знак \"-\" для выхода из меню."""

    title = None
    title = input(f'{question} ("-" для выхода): ')
    if title == '-':
        raise ExitFromMenu()
    return title


def get_date_menu(question: str) -> date:
    """Запрашивает у пользователя дату в формате ДД.ММ.ГГГГ
    или знак \"-\" для выхода из меню."""
    collected_date = None
    while collected_date is None:
        try:
            collected_date = input(f'{question} (ДД.ММ.ГГГГ или "-" для выхода): ')
            collected_date = {
                key: int(value) for key, value
                in DATE_REGEX.fullmatch(collected_date).groupdict().items()
            }
            collected_date = date(**collected_date)
        except AttributeError:
            print('Введена некорректная дата.')
            collected_date = None
    return collected_date


# Стандартный шаблон номерного меню:

def selection_menu(menu_items: dict[str, MenuItem]) -> None:
    """Предлагает пользователю меню с выбором пункта по номеру."""
    while True:
        print('\nДоступные функции:')
        print(*menu_items.values(), sep='\n')
        choice = input('\nВыберите пункт меню: ')
        clear_console()
        if choice == '0':
            raise ExitFromMenu()

        selected = menu_items.get(choice, None)
        if selected is None:
            print('\nТакого пункта меню нет. Попробуйте ещё раз.')
            continue
        try:
            selected()
        except ExitFromMenu:
            pass
