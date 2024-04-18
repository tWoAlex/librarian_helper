-- Самый читаемый автор
-- Выбирается по сумме разных книг, взятых каждым читателейм

SELECT author.name, unique_client_book_combs
FROM
    (SELECT author_id, COUNT(*) as unique_client_book_combs
     FROM
         (SELECT DISTINCT client_id, book_id FROM rent) AS unique_client_book
         INNER JOIN book ON book_id = book.id
     GROUP BY author_id) AS author_unique_book_clients
    INNER JOIN author ON author_id = author.id
ORDER BY unique_client_book_combs DESC
LIMIT 1
