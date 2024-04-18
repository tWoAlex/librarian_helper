-- Следит за тем, чтобы библиотекарь не мог выдать книги, которых нет в наличии

CREATE TRIGGER rents_lesser_then_books
BEFORE INSERT ON rent
BEGIN
    SELECT RAISE(FAIL, "Can't reserve more books than library has")
    FROM book
    WHERE id = NEW.book_id AND quantity = (
        SELECT COUNT(*)
        FROM rent
        GROUP BY book_id, fact_close_date
        HAVING (book_id = NEW.book_id AND fact_close_date IS NULL)
    );
END