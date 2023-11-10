-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer. 
-- DISTINCT is used to eliminate duplicate values from the result set.
-- MOD(ID, 2) = 0 checks if the ID is an even number using the modulo operator (MOD). If the remainder of the division by 2 is 0, it means the number is even.

SELECT DISTINCT CITY FROM STATION
WHERE MOD(ID, 2) = 0;
