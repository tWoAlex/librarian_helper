-- Структура модели жанра.

CREATE TABLE genre (
    id INTEGER PRIMARY KEY ASC,
    title TEXT(50) UNIQUE
)