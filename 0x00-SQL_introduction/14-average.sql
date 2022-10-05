-- Just Average
ALTER TABLE second_table ADD average FLOAT 
Values
(SELECT AVG(score) From second_table)