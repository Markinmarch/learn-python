--запрос на альбомы вышедшие в 2018 году
SELECT "name", "year" FROM album
WHERE "year" = 2018;

--запрос на самый продолжительный трек
SELECT "name", duration FROM track
WHERE duration = (SELECT MAX(duration) FROM track);

--запрос на треки с продолжительность от 3,5 минуты
SELECT "name" FROM track
WHERE duration >= '00:03:30';

--запрос на названия сборников вышедших в период с 2018 по 2020
SELECT "name" FROM collection_track
WHERE "year" >= 2018 AND "year" <= 2020;

--запрос на названия исполнителей из одного слова
--ну тут я прифигел
SELECT "name" FROM artist
WHERE name NOT LIKE '%% %%'

--запрос на название трека с наличием в название "Мой"
select "name" from track
WHERE "name" LIKE '%Мой%' OR LIKE '%мой%'