-- groups
SELECT score 'score' , COUNT(score) 'number' 
FROM second_table 
GROUP BY score
OREDER BY COUNT(score) DESC;