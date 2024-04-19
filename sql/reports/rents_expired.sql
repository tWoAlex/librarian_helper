-- -- Возвращает данные о просроченных, не осуществлённых возвратах в виде
-- -- (имя_читателя, имя_автора, название_книги, ожидаемая_дата_сдачи)


SELECT client.name, author.name, book.title, expected_close_date
FROM
    (SELECT book_id, client_id, expected_close_date FROM rent
     WHERE
        fact_close_date IS NULL AND
        (JULIANDAY("now") - JULIANDAY(expected_close_date)) > 0
    ) AS expired_rent
    INNER JOIN book ON book_id = book.id
    INNER JOIN author ON author_id = author.id
    INNER JOIN client ON client_id = client.id
ORDER BY client.name, author.name, book.title, expected_close_date