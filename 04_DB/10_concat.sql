-- 10_concat.sql
SELECT CONCAT('s', 'q', 'l');

SELECT CONCAT(author_fname, '!!!') FROM books;

SELECT CONCAT(author_fname, ' ', author_lname) FROM books;

SELECT CONCAT(author_fname, ' ', author_lname) AS full_name
FROM books;

SELECT CONCAT('!', 's', 'q', 'l');
SELECT CONCAT_WS('!', 's', 'q', 'l');

SELECT CONCAT_WS('-', title, author_fname, author_lname) AS summary 
FROM books;

