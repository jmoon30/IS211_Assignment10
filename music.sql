PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS artists (
  artist_id INTEGER PRIMARY KEY,
  name      TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS albums (
  album_id     INTEGER PRIMARY KEY,
  artist_id    INTEGER NOT NULL,
  title        TEXT NOT NULL,
  release_year INTEGER,
  FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
  UNIQUE (artist_id, title)
);

CREATE TABLE IF NOT EXISTS songs (
  song_id    INTEGER PRIMARY KEY,
  album_id   INTEGER NOT NULL,
  title      TEXT NOT NULL,
  track_no   INTEGER NOT NULL CHECK (track_no > 0),
  duration_s INTEGER NOT NULL CHECK (duration_s > 0),
  FOREIGN KEY (album_id) REFERENCES albums(album_id) ON DELETE CASCADE,
  UNIQUE (album_id, track_no)
);
