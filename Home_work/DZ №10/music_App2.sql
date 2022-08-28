--создание таблицы альбомов
CREATE TABLE IF NOT EXISTS album (
	id SERIAL INTEGER PRIMARY KEY,
	"name" VARCHAR(40) NOT NULL,
	"year" INTEGER NOT NULL
);

--создание таблицы сборника
CREATE TABLE IF NOT EXISTS collection_track (
	id SERIAL INTEGER PRIMARY KEY,
	"name" VARCHAR(40) NOT NULL,
	"year" INTEGER NOT NULL,
);

--создание таблицы жанров
CREATE TABLE IF NOT EXISTS ganre (
	id SERIAL INTEGER PRIMARY KEY,
	"name" VARCHAR(40) NOT NULL,
);

--создание таблицы песен
CREATE TABLE IF NOT EXISTS track (
	id SERIAL INTEGER PRIMARY KEY,
	"name" VARCHAR(40) NOT NULL,
	duration INTEGER NOT NULL,
	album_id INTEGER NOT NULL,
	FOREIGN KEY (album_id) REFERENCES album(id)
);

--создание промежуточной таблицы исполнитель-альбом
CREATE TABLE IF NOT EXISTS artist_album (
	id SERIAL PRIMARY KEY (id_track, id_album)
	FOREIGN KEY (id_artist) REFERENCES artist(id),
	FOREIGN KEY (id_album) REFERENCES album(id)
);

--создание промежуточной таблицы исполнитель-жанр
CREATE TABLE IF NOT EXISTS artist_ganre (
	id SERIAL PRIMARY KEY (id_artist, id_ganre),
	FOREIGN KEY (id_artist) REFERENCES artist(id),
	FOREIGN KEY (id_ganre) REFERENCES ganre(id)
);

--создание промежуточной таблицы песня-сборник
CREATE TABLE IF NOT EXISTS track_collection (
	id SERIAL INTEGER PRIMARY KEY (id_track, id_collection),
	FOREIGN KEY (id_track) REFERENCES track(id),
	FOREIGN KEY (id_collection) REFERENCES collection_track(id)
);