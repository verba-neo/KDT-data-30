-- 16_etc_functions.sql

SELECT INSERT('Hello justin', 6, 0, ' There');
SELECT INSERT('Hello justin', 6, 3, ' There');

SELECT LEFT('omglol!', 3);
SELECT RIGHT('omglol!', 4);

SELECT LEFT(author_lname, 1) FROM books;
SELECT SUBSTR(author_lname, 1, 1) FROM books;

SELECT REPEAT('ha', 5);

SELECT TRIM('     wow     ');