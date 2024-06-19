-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_genres.name AS genre, tv_genres.id AS number_of_shows
FROM tv_genres, tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_show_genres.genre_id DESC;