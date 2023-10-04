-- practice01.sql

CREATE DATABASE practice;
USE practice;
CREATE TABLE people (
	first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT
);

DESC people;

DROP TABLE people;