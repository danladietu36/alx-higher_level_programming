-- Counts the number of recorda that share the score value
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score;
