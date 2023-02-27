-- Not my genre
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id NOT IN (SELECT id FROM tv_shows WHERE title = 'Dexter') OR tv_show_genres.show_id IS NULL
GROUP BY tv_genres.id
ORDER BY tv_genres.name ASC;
