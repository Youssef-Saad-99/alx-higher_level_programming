-- Selects the genre from the tv_genres table and counts the number of shows linked to each genre from the tv_show_genres table
-- Joins the two tables based on the genre IDs
-- Groups the results by genre
-- Filters out genres that don't have any shows linked
-- Orders the results by the number of shows linked to each genre in descending order
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre ORDER BY number_of_shows DESC;
