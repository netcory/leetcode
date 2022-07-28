SELECT A.id
FROM Weather A
INNER JOIN Weather B
ON TO_DAYS(A.recordDate) - 1 = TO_DAYS(B.recordDate)
WHERE A.temperature > B.temperature