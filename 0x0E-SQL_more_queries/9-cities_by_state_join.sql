-- script lists all cities contained
-- in database 'hbtn_0d_usa'
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = states.id
GROUP BY cities.id ASC;
