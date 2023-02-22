-- Number of shows by genre
SELECT tv_genres.name, COUNT(*) number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY 1
ORDER BY 2 DESC;
