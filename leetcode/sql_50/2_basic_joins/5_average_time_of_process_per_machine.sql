-- Table: Activity
-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | machine_id     | int     |
-- | process_id     | int     |
-- | activity_type  | enum    |
-- | timestamp      | float   |
-- +----------------+---------+

-- There is a factory website that has several machines each running the same number of processes.
-- Write an SQL query to find the average time each machine takes to complete a process.

with united_time as (
	select l.machine_id, l.process_id, l.timestamp start, r.timestamp end
	from Activity l
	inner join Activity r on l.machine_id = r.machine_id and l.process_id = r.process_id
	where l.activity_type = 'start' and r.activity_type = 'end'
	order by machine_id, process_id)
select machine_id, round(avg(end - start), 3) processing_time
from united_time
group by machine_id;
