-- stuff
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id