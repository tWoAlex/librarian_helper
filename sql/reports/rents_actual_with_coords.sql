-- Запрос несортированного списка книг на руках у читателей
-- с данными о книге, читателе и его адресе в виде
-- (имя_автора, название_книги, имя_читателя, долгота, широта)

SELECT author.name, book.title, client.name, longitude, latitude
FROM
    (SELECT book_id, client_id FROM rent
     WHERE fact_close_date IS NULL) AS active_rents
    INNER JOIN book ON book_id = book.id
    INNER JOIN author ON author_id = author.id
    INNER JOIN client ON client_id = client.id
