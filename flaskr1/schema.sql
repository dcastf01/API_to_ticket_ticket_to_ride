-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS players;



CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE game (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	fecha DATETIME,
	fecha_creada TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (Id)
);

CREATE TABLE players (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_game INTEGER NOT NULL,
	nombre TEXT,
	color TEXT,

  FOREIGN KEY(Id_game) REFERENCES  game (id)
);