-- Выгружает список книг строками вида (id, название, имя автора, жанр, количество на балансе)

SELECT
    book.id AS id,
    book.title AS title,
    author.name AS author,
    genre.title AS genre,
    book.quantity AS quantity
FROM
    book
    INNER JOIN author ON book.author_id == author.id
    INNER JOIN genre ON book.genre_id == genre.id
ORDER BY
    author, title, genre
