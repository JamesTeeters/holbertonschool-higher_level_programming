-- Just Average
ALTER TABLE second_table ADD average FLOAT (SELECT AVG(score) From second_table)