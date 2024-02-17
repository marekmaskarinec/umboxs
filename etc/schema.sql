CREATE TABLE packages (
	name VARCHAR(64) PRIMARY KEY NOT NULL,
	token CHAR(128) NOT NULL,
	download_count INT DEFAULT 0
);
