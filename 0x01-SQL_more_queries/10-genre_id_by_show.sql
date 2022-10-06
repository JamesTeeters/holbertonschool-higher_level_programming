-- now for your favorite shows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
INNER JOIN tv_shows_genres
on tv_shows.id = tv_shows_genres.show_id
ORDERED BY tv_shows.title, tv_show_genres.genre_id;