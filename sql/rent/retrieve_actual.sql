-- Запрашивает записи о книгах на руках у читателей
-- и возвращает их в виде (имя автора, название книги, имя читателя, дата выдачи)

SELECT author.name, book.title, client.name, open_date
FROM
    (SELECT * FROM rent WHERE fact_close_date IS NULL) AS active_rents
    INNER JOIN client ON client_id = client.id
    INNER JOIN book ON book_id = book.id
    INNER JOIN author ON book.author_id = author.id
ORDER BY
    author.name, book.title, client.name, open_date
