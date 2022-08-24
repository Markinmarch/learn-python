-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION postgres;
-- public.artist definition

-- Drop table

-- DROP TABLE artist;

CREATE TABLE artist (
	id INTEGER NOT NULL,
	"name" varchar(40) NOT NULL,
	CONSTRAINT artist_pk PRIMARY KEY (id)
);


-- public.collection definition

-- Drop table

-- DROP TABLE collection;

CREATE TABLE collection (
	id INTEGER NOT NULL,
	"name" varchar(40) NOT NULL,
	"year" INTEGER NOT NULL,
	CONSTRAINT collection_pk PRIMARY KEY (id)
);


-- public.ganre definition

-- Drop table

-- DROP TABLE ganre;

CREATE TABLE ganre (
	id INTEGER NOT NULL,
	"name" varchar(40) NOT NULL,
	CONSTRAINT ganre_pk PRIMARY KEY (id)
);


-- public.track definition

-- Drop table

-- DROP TABLE track;

CREATE TABLE track (
	id INTEGER NOT NULL,
	"name" varchar(40) NOT NULL,
	duration time NOT NULL,
	album_name varchar(40) NOT NULL,
	CONSTRAINT track_pk PRIMARY KEY (id)
);


-- public.album definition

-- Drop table

-- DROP TABLE album;

CREATE TABLE album (
	id INTEGER NOT NULL,
	"name" varchar(40) NOT NULL,
	"year" INTEGER NOT NULL,
	id_track INTEGER NOT NULL,
	CONSTRAINT album_pk PRIMARY KEY (id),
	CONSTRAINT album_fk FOREIGN KEY (id_track) REFERENCES track(id)
);


-- public.artist_album definition

-- Drop table

-- DROP TABLE artist_album;

CREATE TABLE artist_album (
	id_artist INTEGER NOT NULL,
	id_album INTEGER NOT NULL,
	CONSTRAINT artist_album_fk FOREIGN KEY (id_artist) REFERENCES artist(id),
	CONSTRAINT artist_album_fk_1 FOREIGN KEY (id_album) REFERENCES album(id)
);


-- public.artist_ganre definition

-- Drop table

-- DROP TABLE artist_ganre;

CREATE TABLE artist_ganre (
	id_artist INTEGER NOT NULL,
	id_ganre INTEGER NOT NULL,
	CONSTRAINT artist_ganre_fk FOREIGN KEY (id_artist) REFERENCES artist(id),
	CONSTRAINT artist_ganre_fk_1 FOREIGN KEY (id_ganre) REFERENCES ganre(id)
);


-- public.track_collection definition

-- Drop table

-- DROP TABLE track_collection;

CREATE TABLE track_collection (
	id_track INTEGER NOT NULL,
	id_collection INTEGER NOT NULL,
	CONSTRAINT newtable_fk FOREIGN KEY (id_track) REFERENCES track(id),
	CONSTRAINT track_collection_fk FOREIGN KEY (id_collection) REFERENCES collection(id)
);
