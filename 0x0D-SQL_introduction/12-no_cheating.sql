-- script updates score of Bob
-- to 10 in the table
UPDATE second_table AS new
SET new.score = 10
WHERE new.name = "Bob";
