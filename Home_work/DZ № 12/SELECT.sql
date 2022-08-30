--количество исполнителей в каждом жанре
SELECT id_ganre, COUNT(*) FROM artist_ganre ag
GROUP BY id_ganre 
ORDER BY COUNT(*) DESC;


--количество треков, вошедших в альбомы 2019-2020 гг.
SELECT a."name", a."year", COUNT(t.id) FROM album a 
JOIN track t ON a.id = t.album_id 
WHERE a."year" BETWEEN 2019 AND 2020
GROUP BY a."name", a."year";


--средняя продолжительность треков по каждому альбому
SELECT a."name", ROUND(AVG(t.duration_)/60, 2) FROM album a 
JOIN track t ON a.id = t.album_id 
GROUP BY a."name";

--все исполнители, которые не выпустили альбомы в 2020 г.
SELECT a."name", a2."year" FROM artist a 
JOIN artist_album aa ON a.id = aa.id_artist 
JOIN album a2 ON aa.id_album = a2.id 
WHERE a2."year" != 2020;

--названия сборников, в которых присутствует конкретный исполнитель
SELECT DISTINCT ct."name" FROM collection_track ct 
JOIN track_collection tc ON ct.id = tc.id_collection 
JOIN track t ON tc.id_track = t.id 
JOIN album a ON t.album_id = a.id 
JOIN artist_album aa ON a.id = aa.id_album 
JOIN artist a2 ON aa.id_artist = a2.id 
WHERE a2."name" LIKE 'Иерарх';


--название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT a."name" FROM album a 
JOIN artist_album aa ON a.id = aa.id_album 
JOIN artist a2 ON aa.id_artist = a2.id 
JOIN artist_ganre ag ON a2.id = ag.id_artist 
GROUP BY a2."name", a."name" 
HAVING count(ag.id_ganre) > 1;


--наименование треков, которые не входят в сборники
SELECT t."name" FROM track t 
LEFT JOIN track_collection tc ON t.id = tc.id_track 
WHERE tc.id_track IS NULL;


--исполнителя(-ей), написавшего самый короткий по продолжительности трек
SELECT a."name", t.duration_ FROM artist a 
JOIN artist_album aa ON a.id = aa.id_artist 
JOIN album a2 ON aa.id_album = a2.id 
JOIN track t ON a2.id = t.album_id 
WHERE t.duration_ IN (SELECT MIN(duration_) FROM track);


--название альбомов, содержащих наименьшее количество треков
SELECT a."name", COUNT(t.id) FROM album a 
JOIN track t ON a.id = t.album_id 
GROUP BY a."name" 
HAVING COUNT(t.id) IN (
	SELECT COUNT (t.id)
	FROM album a
	JOIN track t ON a.id = t.album_id 
	GROUP BY a."name" 
	ORDER BY COUNT(t.id)
	LIMIT 1
	); 