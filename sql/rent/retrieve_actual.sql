-- Запрашивает записи о книгах на руках у читателей
-- и возвращает их в виде (название книги, имя читателя, дата выдачи)

SELECT author.name, book.title, client.name, date
FROM
    (SELECT * FROM rent WHERE closed = 0) AS active_rents
    INNER JOIN client ON client_id = client.id
    INNER JOIN book ON book_id = book.id
    INNER JOIN author ON book.author_id = author.id
ORDER BY
    author.name, book.title, client.name, date
