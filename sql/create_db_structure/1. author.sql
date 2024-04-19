-- Структура модели автора. В текущем контексте требуем уникальное имя.

CREATE TABLE author (
    id INTEGER PRIMARY KEY ASC,
    name TEXT(50) UNIQUE
)