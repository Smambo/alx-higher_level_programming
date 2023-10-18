-- script lists all cities of California
-- that can be found in database 'hbtn_0d_usa'
SELECT cities.id, cities.name FROM cities, states
WHERE cities.id = states.id
ORDER BY cities.id ASC;
