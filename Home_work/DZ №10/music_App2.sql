CREATE SCHEMA public AUTHORIZATION postgres;

CREATE TABLE IF NOT EXISTS artist (
	id serial PRIMARY KEY NOT NULL,
	"name" varchar(40) NOT NULL,
);

CREATE TABLE IF NOT EXISTS track (
	id serial PRIMARY KEY NOT NULL,
	"name" varchar(40) NOT NULL,
	duration time NOT NULL,
	album_name varchar(40) NOT NULL,
);

CREATE TABLE IF NOT EXISTS ganre (
	id serial PRIMARY KEY NOT NULL,
	"name" VARCHAR(40) NOT NULL,
);

CREATE TABLE IF NOT EXISTS collection (
	id serial PRIMARY KEY NOT NULL,
	"name" varchar(40) NOT NULL,
	"year" INTEGER NOT NULL,
);

CREATE TABLE IF NOT EXISTS album (
	id serial PRIMARY KEY NOT NULL,
	"name" VARCHAR(40) NOT NULL,
	"year" INTEGER NOT NULL,
	id_track FOREIGN KEY NOT NULL,
	FOREIGN KEY (id_track) REFERENCES track(id)
);

CREATE TABLE IF NOT EXISTS artist_ganre (
	id_artist INTEGER REFERENCES artist(id),
	id_ganre INTEGER REFERENCES ganre(id),
	CONSTRAINT pk PRIMARY KEY (id_artist, id_ganre)
);

CREATE TABLE IF NOT EXISTS artist_album (
	id_artist INTEGER REFERENCES artist(id),
	id_album INTEGER REFERENCES album(id),
	CONSTRAINT pk PRIMARY KEY (id_artist, id_album)
);

CREATE TABLE IF NOT EXISTS track_collection (
	id_track INTEGER REFERENCES id_track(id),
	id_collection INTEGER REFERENCES id_collection(id),
	CONSTRAINT pk PRIMARY KEY (id_track, id_collection)
);
