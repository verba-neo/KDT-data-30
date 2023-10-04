-- 04_default.sql

CREATE TABLE dogs3 (
	name VARCHAR(20) DEFAULT 'No name',
    age INT DEFAULT 0
);

INSERT INTO dogs3 () VALUES ();

INSERT INTO dogs3 (name) VALUES (NULL);

SELECT * FROM dogs3;

CREATE TABLE dogs4 (
	name VARCHAR(20) NOT NULL DEFAULT 'No name',
    age INT NOT NULL DEFAULT 0
);

-- Error
INSERT INTO dogs4(name) VALUES(NULL);