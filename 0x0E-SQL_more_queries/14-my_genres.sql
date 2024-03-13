-- Selects the genre names from the tv_genres table
-- Joins the tv_genres and tv_show_genres tables based on the genre IDs
-- Filters the records to only include genres linked to the show Dexter, identified by its title in the tv_shows table
-- Orders the results by genre name in ascending order
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;
