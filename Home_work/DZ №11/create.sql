-- DROP SCHEMA music;

CREATE SCHEMA music AUTHORIZATION postgres;

COMMENT ON SCHEMA music IS 'standard public schema';
-- music.artist definition

-- Drop table

-- DROP TABLE artist;

CREATE TABLE IF NOT EXISTS artist (
	id INTEGER PRIMARY KEY NOT NULL,
	"name" VARCHAR(40) NOT NULL
);


-- music.collection_track definition

-- Drop table

-- DROP TABLE collection_track;

CREATE TABLE IF NOT EXISTS collection_track (
	id INTEGER PRIMARY KEY NOT NULL,
	"name" VARCHAR(40) NOT NULL,
	"year" INTEGER NOT NULL
);


-- music.ganre definition

-- Drop table

-- DROP TABLE ganre;

CREATE TABLE IF NOT EXISTS ganre (
	id INTEGER PRIMARY KEY NOT NULL,
	"name" VARCHAR(40) NOT NULL
);


-- music.track definition

-- Drop table

-- DROP TABLE track;

CREATE TABLE IF NOT EXISTS track (
	id INTEGER PRIMARY KEY NOT NULL,
	"name" VARCHAR(40) NOT NULL,
	duration time NOT NULL,
	album_name VARCHAR(40) NOT NULL
);


-- music.album definition

-- Drop table

-- DROP TABLE album;

CREATE TABLE IF NOT EXISTS album (
	id INTEGER PRIMARY KEY NOT NULL,
	"name" VARCHAR(40) NOT NULL,
	"year" INTEGER NOT NULL,
	id_track INTEGER NOT NULL,
	CONSTRAINT album_fk FOREIGN KEY (id_track) REFERENCES track(id)
);


-- music.artist_album definition

-- Drop table

-- DROP TABLE artist_album;

CREATE TABLE IF NOT EXISTS artist_album (
	id_artist INTEGER NOT NULL,
	id_album INTEGER NOT NULL,
	CONSTRAINT artist_album_fk FOREIGN KEY (id_artist) REFERENCES artist(id),
	CONSTRAINT artist_album_fk_1 FOREIGN KEY (id_album) REFERENCES album(id)
);


-- music.artist_ganre definition

-- Drop table

-- DROP TABLE artist_ganre;

CREATE TABLE IF NOT EXISTS artist_ganre (
	id_artist INTEGER NOT NULL,
	id_ganre INTEGER NOT NULL,
	CONSTRAINT artist_ganre_fk FOREIGN KEY (id_artist) REFERENCES artist(id),
	CONSTRAINT artist_ganre_fk_1 FOREIGN KEY (id_ganre) REFERENCES ganre(id)
);


-- music.track_collection definition

-- Drop table

-- DROP TABLE track_collection;

CREATE TABLE IF NOT EXISTS track_collection (
	id_track INTEGER NOT NULL,
	id_collection INTEGER NOT NULL,
	CONSTRAINT newtable_fk FOREIGN KEY (id_track) REFERENCES track(id),
	CONSTRAINT track_collection_fk FOREIGN KEY (id_collection) REFERENCES collection_track(id)
);
