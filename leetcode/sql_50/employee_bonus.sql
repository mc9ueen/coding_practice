-- Table: Employee
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | empId       | int     |
-- | name        | varchar |
-- | supervisor  | int     |
-- | salary      | int     |
-- +-------------+---------+
-- Table: Bonus
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | empId       | int  |
-- | bonus       | int  |
-- +-------------+------+

-- Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.

select e.name, b.bonus
from employee e
left join bonus b on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null;
