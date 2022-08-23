-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION postgres;
-- public.artist definition

-- Drop table

-- DROP TABLE artist;

CREATE TABLE artist (
	id int4 NOT NULL,
	"name" varchar(40) NOT NULL,
	CONSTRAINT artist_pk PRIMARY KEY (id)
);


-- public.track definition

-- Drop table

-- DROP TABLE track;

CREATE TABLE track (
	id int4 NOT NULL,
	"name" varchar(40) NOT NULL,
	duration time NOT NULL,
	album_name varchar(40) NOT NULL,
	CONSTRAINT track_pk PRIMARY KEY (id)
);


-- public.ganre definition

-- Drop table

-- DROP TABLE ganre;

CREATE TABLE ganre (
	id int4 NOT NULL,
	"name" varchar(40) NOT NULL,
	CONSTRAINT ganre_pk PRIMARY KEY (id)
);


-- public.collection definition

-- Drop table

-- DROP TABLE collection;

CREATE TABLE collection (
	id int4 NOT NULL,
	"name" varchar(40) NOT NULL,
	"year" int4 NOT NULL,
	CONSTRAINT collection_pk PRIMARY KEY (id)
);


-- public.album definition

-- Drop table

-- DROP TABLE album;

CREATE TABLE album (
	id int4 NOT NULL,
	"name" varchar(40) NOT NULL,
	"year" int4 NOT NULL,
	id_track int4 NOT NULL,
	CONSTRAINT album_pk PRIMARY KEY (id),
	CONSTRAINT album_fk FOREIGN KEY (id_track) REFERENCES track(id)
);


-- public.artist_ganre definition

-- Drop table

-- DROP TABLE artist_ganre;

CREATE TABLE artist_ganre (
	id_artist int4 NOT NULL,
	id_ganre int4 NOT NULL,
	CONSTRAINT artist_ganre_fk FOREIGN KEY (id_artist) REFERENCES artist(id),
	CONSTRAINT artist_ganre_fk_1 FOREIGN KEY (id_ganre) REFERENCES ganre(id)
);


-- public.artist_album definition

-- Drop table

-- DROP TABLE artist_album;

CREATE TABLE artist_album (
	id_artist int4 NOT NULL,
	id_album int4 NOT NULL,
	CONSTRAINT artist_album_fk FOREIGN KEY (id_artist) REFERENCES artist(id),
	CONSTRAINT artist_album_fk_1 FOREIGN KEY (id_album) REFERENCES album(id)
);


-- public.track_collection definition

-- Drop table

-- DROP TABLE track_collection;

CREATE TABLE track_collection (
	id_track int4 NOT NULL,
	id_collection int4 NOT NULL,
	CONSTRAINT newtable_fk FOREIGN KEY (id_track) REFERENCES track(id),
	CONSTRAINT track_collection_fk FOREIGN KEY (id_collection) REFERENCES collection(id)
);
