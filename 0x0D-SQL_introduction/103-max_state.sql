-- Max temp
SELECT state, MAX(value) max_temp
FROM temperatures
GROUP BY 1
ORDER BY 1;
