-- use database hbtn_0d_usa 
USE hbtn_0d_usa;

-- lists all the cities of California
SELECT cities.name 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
) 
ORDER BY cities.id ASC;
