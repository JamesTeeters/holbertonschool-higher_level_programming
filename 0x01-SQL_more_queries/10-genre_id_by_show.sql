-- now for your favorite shows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tvshows
INNER JOIN tv_shows_genres
on tv_shows.id = tv_shows_genres.show_id
ORDERED BY tv_shows.title, tv_show_genres.genre_id;