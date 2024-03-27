-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre
FROM tv_show_genres sg
JOIN tv_shows s ON sg.show_id = s.id
JOIN genres g ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
