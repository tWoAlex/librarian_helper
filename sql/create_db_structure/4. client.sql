-- Структура модели читателя.
-- В текущем контексте, когда нам известны только имя и адрес,
-- требуем уникальное имя владельца и обязательный адрес.

CREATE TABLE client (
    id INTEGER PRIMARY KEY ASC,
    name TEXT(50) UNIQUE,
    longitude REAL NOT NULL,
    latitude REAL NOT NULL
)