--вносим данные в таблицу исполнителей
INSERT INTO artist(id, "name")
VALUES(1, 'Сигизмунд');

INSERT INTO artist(id, "name")
VALUES(2, 'Иерарх');

INSERT INTO artist(id, "name")
VALUES(3, 'Тетропах');

INSERT INTO artist(id, "name")
VALUES(4, 'Музыкальный трубопровод');

INSERT INTO artist(id, "name")
VALUES(5, 'Гитара без струн');

INSERT INTO artist(id, "name")
VALUES(6, 'Играем на гуслях');

INSERT INTO artist(id, "name")
VALUES(7, 'Гуси-убийцы');

INSERT INTO artist(id, "name")
VALUES(8, 'Цирковая опера');

--вносим данные в таблицу жанров
INSERT INTO ganre(id, "name")
VALUES(1, 'Тяжелейший рок');

INSERT INTO ganre(id, "name")
VALUES(2, 'Поп-фристайл');

INSERT INTO ganre(id, "name")
VALUES(3, 'Рок-н-ролики');

INSERT INTO ganre(id, "name")
VALUES(4, 'Дворовые песни алкашей');

INSERT INTO ganre(id, "name")
VALUES(5, 'Бабкин крик');

--вносим данные в таблицу альбомов
INSERT INTO album(id, "name", "year")
VALUES(1, 'Дворовые коты орут не только в марте', 2022);

INSERT INTO album(id, "name", "year")
VALUES(2, 'Подайте на алкашку', 2022);

INSERT INTO album(id, "name", "year")
VALUES(3, 'Дворовые коты орут не только в марте', 2022);

--это я внёс случайно одинаковыые названия, пришлось обновить
UPDATE album 
SET "name" = 'Двоюродные соседи'
WHERE id = 3;

INSERT INTO album(id, "name", "year")
VALUES(4, 'Собаки лаяли под окном', 2022);

INSERT INTO album(id, "name", "year")
VALUES(5, 'Перламутровые закаты', 2022);

INSERT INTO album(id, "name", "year")
VALUES(6, 'Глазеющий на топлес', 2022);

INSERT INTO album(id, "name", "year")
VALUES(7, 'ДжигитАЛ', 2022);

INSERT INTO album(id, "name", "year")
VALUES(8, 'А улитки громко шепчут', 2022);

INSERT INTO album(id, "name", "year")
VALUES(9, 'Транспортный коллапс', 2022);

INSERT INTO album(id, "name", "year")
VALUES(10, 'На очереди к врачу', 2022);

--вносим данные в таблицу треков
INSERT INTO track (id, "name", duration)
VALUES(1, 'Кот Фёдор неустанно орёт под моим окном', '03:12');

INSERT INTO track (id, "name", duration)
VALUES(2, 'Наконец-то кота Фёдора кастрировали', '01:10');

INSERT INTO track (id, "name", duration)
VALUES(3, 'Кот Фёдор неустанно орёт под моим окном', '03:12');

INSERT INTO track (id, "name", duration)
VALUES(4, 'Протянул руку, чтобы не протянуть ноги', '02:15:00');

INSERT INTO track (id, "name", duration)
VALUES(5, 'Ты так вкусна, Красная шапочка', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(6, 'Вкусно? Ну вкусно!', '01:15');

INSERT INTO track (id, "name", duration)
VALUES(7, 'Сосед напротив', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(8, 'Сосед слева', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(9, 'Сосед справа', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(10, 'Бездомный пёс съел кота Фёдора', '01:00');

INSERT INTO track (id, "name", duration)
VALUES(11, 'Бездомного пса кастрировали', '01:00');

INSERT INTO track (id, "name", duration)
VALUES(12, 'Пёс Фёдор', '03:20');

INSERT INTO track (id, "name", duration)
VALUES(13, 'Бабка перепутала грибы', '01:05');

INSERT INTO track (id, "name", duration)
VALUES(14, 'Дед сварил новый самогон', '10:15');

INSERT INTO track (id, "name", duration)
VALUES(15, 'Больше не вижу заката и деда', '02:12');

INSERT INTO track (id, "name", duration)
VALUES(16, 'Простились с дедом', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(17, 'У меня появились усы', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(18, 'Я на пляже, топлес-шмоплес', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(19, 'Почему мне никто не даёт', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(20, 'Сочный спэлый арбуз', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(21, 'Завёл себе ТАЗ', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(22, 'Не дам людям ночью спать', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(23, 'После дождя', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(24, 'Не дави менеая-э', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(25, 'Почему снова проезд подорожал', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(26, 'Нет свободных мест', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(27, 'Бегу поперёк скоростной трассы', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(28, 'У меня талон на 12-00', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(29, 'Доктор, мне долго осталось?', '03:00');

INSERT INTO track (id, "name", duration)
VALUES(30, 'Я буду долго жить, на хату не надейтесь', '03:00');

--вносим данные в таблицу сборников
INSERT INTO collection_track (id, "name", "year")
VALUES(1, 'Контраст', 2022);

INSERT INTO collection_track (id, "name", "year")
VALUES(2, 'Опять 25', 2022);

INSERT INTO collection_track (id, "name", "year")
VALUES(3, 'Старые и пьяные', 2022);

INSERT INTO collection_track (id, "name", "year")
VALUES(4, 'Лежать на боку', 2022);

INSERT INTO collection_track (id, "name", "year")
VALUES(5, 'Почему?', 2022);

INSERT INTO collection_track (id, "name", "year")
VALUES(6, 'Больше не буду', 2022);

INSERT INTO collection_track (id, "name", "year")
VALUES(7, 'Танцы с бубном', 2022);

INSERT INTO collection_track (id, "name", "year")
VALUES(8, 'Под подъездом', 2022);


--затем я прочитал второе задание - ведь я человек последовательный >:-0
--обновляю годы выхода в таблице альбомов
UPDATE album
SET "year" = 2018
WHERE id = 1;

UPDATE album
SET "year" = 2018
WHERE id = 2;

UPDATE album
SET "year" = 2018
WHERE id = 3;

UPDATE album
SET "year" = 2019
WHERE id = 4;

UPDATE album
SET "year" = 2019
WHERE id = 5;

UPDATE album
SET "year" = 2020
WHERE id = 6;

UPDATE album
SET "year" = 2020
WHERE id = 7;

UPDATE album
SET "year" = 2021
WHERE id = 8;

--обновляем годы выхода в таблице сборников
UPDATE collection_track 
SET "year" = 2018
WHERE id = 1;

UPDATE collection_track
SET "year" = 2018
WHERE id = 2;

UPDATE collection_track
SET "year" = 2018
WHERE id = 3;

UPDATE collection_track
SET "year" = 2019
WHERE id = 4;

UPDATE collection_track
SET "year" = 2019
WHERE id = 5;

UPDATE collection_track
SET "year" = 2020
WHERE id = 6;

UPDATE collection_track
SET "year" = 2020
WHERE id = 7;

UPDATE collection_track
SET "year" = 2021
WHERE id = 8;

--ну и корректируем некоторые данные, чтобы вписатсья во второе задание
UPDATE track
SET "name" = 'Мой дед варит самогон'
WHERE id = 14;

--а теперь ещё и научились пользоваться типом данных time
UPDATE track
SET duration = '00:03:15'
WHERE id = 1

UPDATE track
SET duration = '00:03:15'
WHERE id = 2

UPDATE track
SET duration = '00:03:15'
WHERE id = 3

UPDATE track
SET duration = '00:03:15'
WHERE id = 4

UPDATE track
SET duration = '00:03:15'
WHERE id = 5

UPDATE track
SET duration = '00:03:15'
WHERE id = 6

UPDATE track
SET duration = '00:03:15'
WHERE id = 7

UPDATE track
SET duration = '00:03:20'
WHERE id = 8

UPDATE track
SET duration = '00:03:20'
WHERE id = 9

UPDATE track
SET duration = '00:03:20'
WHERE id = 10

UPDATE track
SET duration = '00:03:20'
WHERE id = 11

UPDATE track
SET duration = '00:03:20'
WHERE id = 12

UPDATE track
SET duration = '00:03:20'
WHERE id = 13

UPDATE track
SET duration = '00:03:20'
WHERE id = 14

UPDATE track
SET duration = '00:03:20'
WHERE id = 15

UPDATE track
SET duration = '00:03:40'
WHERE id = 16

UPDATE track
SET duration = '00:03:40'
WHERE id = 17

UPDATE track
SET duration = '00:03:40'
WHERE id = 18

UPDATE track
SET duration = '00:03:40'
WHERE id = 19

UPDATE track
SET duration = '00:03:40'
WHERE id = 20

UPDATE track
SET duration = '00:03:40'
WHERE id = 21

UPDATE track
SET duration = '00:03:40'
WHERE id = 22

UPDATE track
SET duration = '00:03:40'
WHERE id = 23

UPDATE track
SET duration = '00:03:40'
WHERE id = 24

UPDATE track
SET duration = '00:01:10'
WHERE id = 25

UPDATE track
SET duration = '00:01:10'
WHERE id = 26

UPDATE track
SET duration = '00:01:10'
WHERE id = 27

UPDATE track
SET duration = '00:01:10'
WHERE id = 28

UPDATE track
SET duration = '00:01:10'
WHERE id = 29

UPDATE track
SET duration = '00:4:10'
WHERE id = 30