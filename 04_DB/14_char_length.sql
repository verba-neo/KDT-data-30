-- 14_char_length.sql

SELECT CHAR_LENGTH('qwer');

SELECT LENGTH('가나다');  -- 동작 이상함
SELECT CHAR_LENGTH('가나다');

SELECT CHAR_LENGTH(title) AS 'title length', title
FROM books;