select p.project_id, round(sum(experience_years) / count(experience_years), 2) average_years
from Project p
join Employee e on p.employee_id = e.employee_id
group by p.project_id