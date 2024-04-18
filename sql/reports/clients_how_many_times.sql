-- Сколько раз каждый читатель брал книги за всё время

SELECT client.name, COUNT(*) AS times
FROM
    rent INNER JOIN client ON rent.client_id = client.id
GROUP BY client.id
ORDER BY client.name