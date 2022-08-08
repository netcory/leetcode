# Write your MySQL query statement below
SELECT Department, Employee, Salary FROM
            (SELECT T2.name AS Department, T1.name AS Employee
            ,T1.salary AS Salary
            ,RANK() OVER (PARTITION BY T2.name ORDER BY T1.salary DESC) AS 'Rank'
            FROM Employee T1
            JOIN Department T2
            ON T1.departmentId = T2.id
            ) AS T
WHERE T.Rank = 1