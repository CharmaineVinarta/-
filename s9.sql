-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table. 
-- For example, if there are three records in the table with CITY values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'. 
-- The query returns , because total_number_of_records - total_number_of_unique_cities = 3 - 2 = 1

SELECT COUNT(CITY) - (SELECT COUNT(DISTINCT CITY) FROM STATION) AS Difference
FROM STATION;
