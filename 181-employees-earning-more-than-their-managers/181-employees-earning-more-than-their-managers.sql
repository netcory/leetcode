# Write your MySQL query statement below
SELECT A.name AS employee
FROM Employee A
LEFT OUTER JOIN Employee B
ON A.managerID = B.id
WHERE A.salary > B.salary