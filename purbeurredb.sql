CREATE DATABASE PurBeurreDb;


CREATE TABLE snacks(
    id SMALLINT NOT NULL AUTO_INCREMENT,
    Product_name VARCHAR(250) NOT NULL,
    nova_group INT(1) NOT NULL,
    countries_tags TEXT(1000) NOT NULL,
    stores_tags TEXT(1000),
    energy INT(10) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

CREATE TABLE boissons(
    id SMALLINT NOT NULL AUTO_INCREMENT,
    Product_name VARCHAR(250) NOT NULL,
    nova_group INT(1) NOT NULL,
    countries_tags TEXT(1000) NOT NULL,
    stores_tags TEXT(1000),
    energy INT(10) NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

CREATE TABLE viandes(
    id SMALLINT NOT NULL AUTO_INCREMENT,
    Product_name VARCHAR(250) NOT NULL,
    nova_group INT(1) NOT NULL,
    countries_tags TEXT(1000) NOT NULL,
    stores_tags TEXT(1000),
    energy INT(10) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

CREATE TABLE charcuteries(
    id SMALLINT NOT NULL AUTO_INCREMENT,
    Product_name VARCHAR(250) NOT NULL,
    nova_group INT(1) NOT NULL,
    countries_tags TEXT(1000) NOT NULL,
    stores_tags TEXT(1000),
    energy INT(10) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

CREATE TABLE desserts(
    id SMALLINT NOT NULL AUTO_INCREMENT,
    Product_name VARCHAR(250) NOT NULL,
    nova_group INT(1) NOT NULL,
    countries_tags TEXT(1000) NOT NULL,
    stores_tags TEXT(1000),
    energy INT(10) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;


DROP TABLE boissons;
DROP TABLE snacks;
DROP TABLE viandes;
DROP TABLE desserts;
DROP TABLE charcuteries;



SELECT * FROM boissons;
SELECT * FROM snacks;
SELECT * FROM viandes;
SELECT * FROM desserts;
SELECT * FROM charcuteries;

