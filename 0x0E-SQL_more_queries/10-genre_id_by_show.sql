-- Selects the title of TV shows and their associated genre IDs from the tables tv_shows and tv_show_genres
-- Joins the two tables based on the TV show IDs
-- Orders the results by TV show title and genre ID in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
