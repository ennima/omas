CREATE TABLE books(
	book_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	publisher_id INTEGER UNSIGNED NOT NULL,
	titulo VARCHAR(60) NOT NULL,
	autor VARCHAR(100) NOT NULL,
	price DECIMAL(5,2)
);

CREATE TABLE publishers(
	publisher_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	country VARCHAR(20)
);

CREATE TABLE users(
	user_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE
);



INSERT INTO `books` (`book_id`, `field_1`, `field_2`, `fecha`, `hora`, `tiempo`, `field_3`) VALUES ('1', '2', '3', '2016-10-05', '04:00:00', '2016-10-14 02:12:16', '5.3');

UPDATE `books` SET `field_1` = '11' WHERE `books`.`book_id` = 2;

DELETE FROM `books` WHERE `books`.`book_id` = 3