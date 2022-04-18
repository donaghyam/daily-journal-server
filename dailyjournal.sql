-- This is a text file to hold the SQL commands to interact with the database

CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`entry`	TEXT NOT NULL,
	`mood_id`	INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`    TEXT NOT NULL
);

CREATE TABLE `Tags` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL
);

CREATE TABLE `Entry_Tag` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id`	INTEGER NOT NULL,
    `tag_id`	INTEGER NOT NULL,
    FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

INSERT INTO `Moods` VALUES (null, "Bored");
INSERT INTO `Moods` VALUES (null, "Angry");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Content");
INSERT INTO `Moods` VALUES (null, "Happy");

INSERT INTO `Entries` VALUES (null, "Getting more familiar with SQL", 5);
INSERT INTO `Entries` VALUES (null, "How has anyone really been far as decided to do want to do look more like?", 4);
INSERT INTO `Entries` VALUES (null, "Leanring Python", 3);
INSERT INTO `Entries` VALUES (null, "The arsonist had oddly shaped feet", 2);
INSERT INTO `Entries` VALUES (null, "How now brown cow", 1);

INSERT INTO `Tags` VALUES (null, "Python");
INSERT INTO `Tags` VALUES (null, "JavaScript");
INSERT INTO `Tags` VALUES (null, "SQL");
INSERT INTO `Tags` VALUES (null, "Data");
INSERT INTO `Tags` VALUES (null, "Syntax");