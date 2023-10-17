-- practice07.sql

-- 1
SELECT REPLACE(title, ' ', '->') AS title FROM books;

-- 2
SELECT author_lname AS forwards, REVERSE(author_lname) AS backwards
FROM books;

-- 3
SELECT UPPER(CONCAT(author_fname, ' ', author_lname)) AS 'full name in caps' 
FROM books;

SELECT UPPER(CONCAT_WS(' ', author_fname, author_lname)) AS 'full name in caps' 
FROM books;

-- 4
SELECT CONCAT(title, ' was released in ', released_year) AS summary 
FROM books;

-- 5
SELECT title, CHAR_LENGTH(title) AS 'character count' 
FROM books;

-- 6
SELECT
	CONCAT() AS 'short title',
    CONCAT() AS 'author',
    CONCAT() AS 'quantity'
FROM books;