CREATE TABLE book (
    id INTEGER PRIMARY KEY ASC,
    author_id INT NOT NULL,
    genre_id INT NOT NULL,
    title TEXT(50),
    quantity INT CHECK(quantity >= 0),

    FOREIGN KEY (author_id) REFERENCES author (id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genre (id) ON DELETE CASCADE
)
