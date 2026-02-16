# Write your MySQL query statement below
SELECT m.name as Employee from Employee e join Employee m on e.id=m.managerId where e.salary<=m.salary;