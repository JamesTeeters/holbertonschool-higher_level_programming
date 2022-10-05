-- groups
SELECT score, COUNT(score) 'number' 
FROM second_table 
GROUP BY score
ORDER BY COUNT(score) DESC;