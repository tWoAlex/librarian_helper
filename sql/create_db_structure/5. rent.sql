CREATE TABLE rent (
    id INTEGER PRIMARY KEY ASC,
    book_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    date DATE,
    closed INTEGER,

    FOREIGN KEY (book_id) REFERENCES book (id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES client (id) ON DELETE CASCADE
)
