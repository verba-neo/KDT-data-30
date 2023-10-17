-- 13_reverse.sql

SELECT REVERSE('apple');

SELECT CONCAT(author_fname, REVERSE(author_fname)) AS strange_name
FROM books;