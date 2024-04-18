-- Самый популярный жанр у каждого читателя

WITH
client_genre_counts AS (
    SELECT
        client_id, client.name AS client_name,
        genre_id, genre.title AS genre_title,
        COUNT(*) AS client_genre_count
    FROM
        (SELECT DISTINCT client_id, book_id FROM rent) AS unique_book_client
        INNER JOIN book ON book_id = book.id
        INNER JOIN genre ON genre_id = genre.id
        INNER JOIN client ON client_id = client.id
    GROUP BY client_id, genre_id
),
client_max_genre_counts AS (
    SELECT client_id, MAX(client_genre_count) as max_genre_count
    FROM client_genre_counts
    GROUP BY client_id
)

SELECT client_name, genre_title, client_genre_count
FROM
    client_genre_counts INNER JOIN client_max_genre_counts
    ON (
        client_genre_counts.client_id = client_max_genre_counts.client_id
        AND
        client_genre_counts.client_genre_count = client_max_genre_counts.max_genre_count
    )
ORDER BY client_name, genre_title, client_genre_count
