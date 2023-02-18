-- High temp
SELECT city, AVG(value) avg_temp
FROM temperatures
WHERE month in (7, 8)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 3;
