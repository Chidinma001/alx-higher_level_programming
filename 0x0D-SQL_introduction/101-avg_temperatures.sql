-- DISPLAY AVG TEMP
SELECT city, AVG(value) avg_temp
FROM temperatures
GROUP BY 1
ORDER BY 2 DESC;
