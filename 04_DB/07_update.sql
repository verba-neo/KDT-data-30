-- 07_update.sql

-- UPDATE <table> SET <col>=<val> WHERE <condition>;

SELECT * FROM cats;

UPDATE cats SET age=14 WHERE name='Misty';
UPDATE cats SET age=age+1 WHERE name='Jackson';
