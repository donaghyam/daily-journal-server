-- This is a text file to hold the SQL commands to interact with the database

CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`entry`	TEXT NOT NULL,
	`mood_id`	INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`    TEXT NOT NULL
);

INSERT INTO `Mood` VALUES (null, "Bored");
INSERT INTO `Mood` VALUES (null, "Angry");
INSERT INTO `Mood` VALUES (null, "Sad");
INSERT INTO `Mood` VALUES (null, "Content");
INSERT INTO `Mood` VALUES (null, "Happy");

INSERT INTO `Entries` VALUES (null, "Getting more familiar with SQL", 5);
INSERT INTO `Entries` VALUES (null, "How has anyone really been far as decided to do want to do look more like?", 4);
INSERT INTO `Entries` VALUES (null, "Leanring Python", 3);
INSERT INTO `Entries` VALUES (null, "The arsonist had oddly shaped feet", 2);
INSERT INTO `Entries` VALUES (null, "How now brown cow", 1);