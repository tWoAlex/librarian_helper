-- Сколько уникальных книг брал каждый читатель за всё время

SELECT client.name, COUNT(*) AS distinct_books
FROM
    (SELECT DISTINCT client_id, book_id
     FROM rent) AS distinct_client_book
    INNER JOIN client
    ON client_id = client.id
GROUP BY client.id
ORDER BY client.name, distinct_books
