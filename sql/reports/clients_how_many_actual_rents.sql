-- Сколько сейчас книг на руках у каждого читателя

SELECT client.name, COUNT(*) as rents_by_client
FROM
    (SELECT * FROM rent WHERE fact_close_date IS NULL) AS actual_rents
    INNER JOIN client ON client_id = client.id
GROUP BY client.id
HAVING rents_by_client > 0
ORDER BY client.name, rents_by_client