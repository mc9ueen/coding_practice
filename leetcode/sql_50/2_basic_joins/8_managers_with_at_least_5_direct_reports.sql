-- Table: Employee
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | department  | varchar |
-- | managerId   | int     |
-- +-------------+---------+

-- Write a solution to find managers with at least five direct reports.
-- Return the result table in any order.

-- Using subquery
select name
from employee
where id in (
	select managerId
    from employee
    group by managerId
    having managerId is not null and count(*) >= 5
    );

-- Using join
select e.name
from employee e
left join employee m on e.id = m.managerId
group by e.id, e.name
having count(*) >= 5;