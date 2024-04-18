-- Дата последнего посещения читателем библиотеки

SELECT client.name, last_visit
FROM
    (SELECT client_id, MAX(date) AS last_visit
     FROM rent GROUP BY client_id) AS last_visits
    INNER JOIN client ON client_id = client.id
ORDER BY client.name, last_visit
