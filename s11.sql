-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
-- 

SELECT CITY FROM STATION
WHERE CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' OR CITY LIKE 'U%';

or, this code also would work

SELECT CITY FROM STATION
WHERE UPPER(SUBSTR(CITY, 1, 1)) IN ('A', 'E', 'I', 'O', 'U');
