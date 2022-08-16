-- DROP SCHEMA "App01";

CREATE SCHEMA "App01" AUTHORIZATION postgres;
-- "App01".track definition

-- Drop table

-- DROP TABLE track;

CREATE TABLE track (
	id int4 NOT NULL,
	track_name varchar(40) NOT NULL,
	duration time NOT NULL,
	album_name varchar(40) NOT NULL,
	CONSTRAINT id_track PRIMARY KEY (id)
);


-- "App01".collection definition

-- Drop table

-- DROP TABLE collection;

CREATE TABLE collection (
	id int4 NOT NULL,
	collection_name varchar(40) NOT NULL,
	collection_year int4 NOT NULL,
	id_track int4 NOT NULL,
	CONSTRAINT id_collection PRIMARY KEY (id),
	CONSTRAINT collection_fk FOREIGN KEY (id_track) REFERENCES track(id)
);


-- "App01".album definition

-- Drop table

-- DROP TABLE album;

CREATE TABLE album (
	id int4 NOT NULL,
	album_name varchar(40) NOT NULL,
	album_year int4 NOT NULL,
	id_artist int4 NOT NULL,
	id_track int4 NOT NULL,
	CONSTRAINT id_album PRIMARY KEY (id)
);


-- "App01".artist definition

-- Drop table

-- DROP TABLE artist;

CREATE TABLE artist (
	id int4 NOT NULL,
	artist_name varchar(40) NOT NULL,
	id_ganre int4 NOT NULL,
	id_album int4 NOT NULL,
	CONSTRAINT id_artist PRIMARY KEY (id)
);


-- "App01".ganre definition

-- Drop table

-- DROP TABLE ganre;

CREATE TABLE ganre (
	id int4 NOT NULL,
	ganre_name varchar(40) NOT NULL,
	id_artist int4 NOT NULL,
	CONSTRAINT id_ganre PRIMARY KEY (id)
);


-- "App01".album foreign keys

ALTER TABLE "App01".album ADD CONSTRAINT album_fk FOREIGN KEY (id_artist) REFERENCES artist(id);
ALTER TABLE "App01".album ADD CONSTRAINT album_fk_1 FOREIGN KEY (id_track) REFERENCES track(id);


-- "App01".artist foreign keys

ALTER TABLE "App01".artist ADD CONSTRAINT artist_fk FOREIGN KEY (id_ganre) REFERENCES ganre(id);
ALTER TABLE "App01".artist ADD CONSTRAINT artist_fk_1 FOREIGN KEY (id_album) REFERENCES album(id);


-- "App01".ganre foreign keys

ALTER TABLE "App01".ganre ADD CONSTRAINT ganre_fk FOREIGN KEY (id_artist) REFERENCES artist(id);
