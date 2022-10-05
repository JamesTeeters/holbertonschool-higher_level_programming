-- Just Average
INSERT INTO second_table (average)
VALUES
(SELECT AVG(score) From second_table)