-- Table: Students
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | student_id    | int     |
-- | student_name  | varchar |
-- +---------------+---------+
-- Table: Subjects
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | subject_name | varchar |
-- +--------------+---------+
-- Table: Examinations
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | student_id   | int     |
-- | subject_name | varchar |
-- +--------------+---------+

-- Write a solution to find the number of times each student attended each exam.
-- Return the result table ordered by student_id and subject_name.

with subjects_for_each_student as (
    select student_id, student_name, subject_name
    from students
    cross join subjects)
select sfes.student_id, sfes.student_name, sfes.subject_name, coalesce(count(exs.subject_name), 0)
from subjects_for_each_student sfes
left join examinations exs on sfes.student_id = exs.student_id and sfes.subject_name = exs.subject_name
group by sfes.student_id, sfes.student_name, sfes.subject_name
order by sfes.student_id, sfes.subject_name; 
