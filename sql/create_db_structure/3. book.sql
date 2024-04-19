-- Структура модели книги.
-- В текущем контексте считаем, что у одного автора
-- все имена произведений должны быть уникальны.

CREATE TABLE book (
    id INTEGER PRIMARY KEY ASC,
    author_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    title TEXT(50),
    quantity INTEGER CHECK(quantity >= 0),

    UNIQUE (author_id, title) ON CONFLICT FAIL
    FOREIGN KEY (author_id) REFERENCES author (id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genre (id) ON DELETE CASCADE
)
