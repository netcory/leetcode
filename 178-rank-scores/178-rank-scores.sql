# Write your MySQL query statement below
SELECT A.score, B.rank
FROM Scores A
LEFT OUTER JOIN (
                    SELECT score, row_number() over(ORDER BY score DESC) AS 'rank'
                    FROM Scores
                    GROUP BY score
                ) B
ON A.score = B.score
ORDER BY score DESC