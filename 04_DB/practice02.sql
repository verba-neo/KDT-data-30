-- practice02.sql

USE practice;
CREATE TABLE people(
	first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT
);

DESC people;

INSERT INTO people (first_name, last_name, age)
VALUES
	('철수', '김', 20),
    ('영희', '박', 21),
    ('준수', '이', 22);

SELECT * FROM people;