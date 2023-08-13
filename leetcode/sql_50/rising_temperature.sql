select distinct td.id
from weather td
inner join weather ystd on datediff(td.recordDate, ystd.recordDate) = 1
where td.temperature > ystd.temperature;