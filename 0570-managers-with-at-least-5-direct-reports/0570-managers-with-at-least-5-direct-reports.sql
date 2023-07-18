# Write your MySQL query statement below
select name
from Employee E
JOIN (
select managerId
from Employee
group by  managerId
having count(*) > 4
) T
on E.id = T.managerId
