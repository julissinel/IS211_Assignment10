
CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    artist_name varchar(255) NOT NULL
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    album_title varchar(255) NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

CREATE TABLE track (
    id INTEGER PRIMARY KEY,
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    track_title varchar(255) NOT NULL,
    track_length INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album(id)
);
