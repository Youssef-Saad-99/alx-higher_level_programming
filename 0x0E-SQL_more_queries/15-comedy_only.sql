-- Selects the show titles from the tv_shows table
-- Joins the tv_shows, tv_show_genres, and tv_genres tables based on the genre IDs
-- Filters the records to only include shows with the genre Comedy, identified by its name in the tv_genres table
-- Orders the results by show title in ascending order
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;
