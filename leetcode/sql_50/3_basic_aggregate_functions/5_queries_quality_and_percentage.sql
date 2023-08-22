select query_name,
       round(sum(l.rating / l.position) / count(l.query_name), 2) quality,
       round( ... count(query_name) * 100, 2) poor_query_percentage
from Queries l
join Queries r join l.query_name = r.query_name
group by query_name