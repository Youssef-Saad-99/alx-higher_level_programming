-- Selects the show title and genre name from the tv_shows, tv_show_genres, and tv_genres tables
-- Joins the tv_shows and tv_show_genres tables based on the show IDs
-- Joins the tv_show_genres and tv_genres tables based on the genre IDs
-- Uses LEFT JOIN to include shows without a genre, displaying NULL in the genre column
-- Orders the results by show title and genre name in ascending order
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
