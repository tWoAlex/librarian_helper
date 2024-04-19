-- Структура записи о выдаче книги.

CREATE TABLE rent (
    id INTEGER PRIMARY KEY ASC,
    book_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    open_date DATE NOT NULL,
    expected_close_date DATE NOT NULL,
    fact_close_date DATE,

    FOREIGN KEY (book_id) REFERENCES book (id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES client (id) ON DELETE CASCADE
)
