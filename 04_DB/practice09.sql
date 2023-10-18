-- practice09.sql

-- 1.
SELECT COUNT(*) FROM books;

-- 2.
SELECT released_year, COUNT(*) 
FROM books GROUP BY released_year ORDER BY released_year;

-- 3.
SELECT SUM(stock_quantity) FROM books;

-- 4.
SELECT 
	author_fname,
    author_lname,
    AVG(released_year)
FROM books
GROUP BY author_fname, author_lname;

-- 5.
SELECT 
	CONCAT(author_fname, ' ', author_lname) AS 'full name',
    pages
FROM books
WHERE pages = (SELECT MAX(pages) FROM books);

-- 6.
SELECT
	released_year AS 'year',
    COUNT(*) AS '# books',
    AVG(pages) AS 'avg pages'
FROM books
GROUP BY released_year
ORDER BY released_year;
