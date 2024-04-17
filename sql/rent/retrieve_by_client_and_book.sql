SELECT id, date FROM rent
WHERE client_id={client_id} AND book_id={book_id}
ORDER BY id
LIMIT 1
