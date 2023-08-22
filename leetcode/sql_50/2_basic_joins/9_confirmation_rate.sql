-- Table: Signups
-- +----------------+----------+
-- | Column Name    | Type     |
-- +----------------+----------+
-- | user_id        | int      |
-- | time_stamp     | datetime |
-- +----------------+----------+ 
-- Table: Confirmations
-- +----------------+----------+
-- | Column Name    | Type     |
-- +----------------+----------+
-- | user_id        | int      |
-- | time_stamp     | datetime |
-- | action         | ENUM     |
-- +----------------+----------+

-- The confirmation rate of a user is the number of 'confirmed' messages
-- divided by the total number of requested confirmation messages.
-- The confirmation rate of a user that did not request any confirmation messages is 0.
-- Round the confirmation rate to two decimal places.

-- Write an SQL query to find the confirmation rate of each user.

select s.user_id, round(sum(if(action = 'timeout' or action is null, 0, 1)) / count(s.user_id), 2) confirmation_rate
from Signups s
left join Confirmations c on s.user_id = c.user_id
group by user_id
