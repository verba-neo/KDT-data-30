-- 15_upper_lower.sql

SELECT UPPER('hello');
SELECT LOWER('WORLD');

SELECT UPPER(title) AS upper_title FROM books;
SELECT LOWER(title) AS upper_title FROM books;

-- 'I LOVE <BOOK_TITLE>!!!'
SELECT UPPER(CONCAT('i love ', title, '!!!')) FROM books;
SELECT CONCAT('I LOVE ', UPPER(title), '!!!') FROM books;
