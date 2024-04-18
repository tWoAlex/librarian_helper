-- Самые популярные жанры у читателей

SELECT genre.title, COUNT(*) as unique_client_book
FROM
    (SELECT DISTINCT client_id, book_id FROM rent) AS unique_client_book
    INNER JOIN book ON book_id = book.id
    INNER JOIN genre ON book.genre_id = genre.id
GROUP BY genre_id
ORDER BY unique_client_book DESC, genre.title ASC
