CREATE DATABASE PurBeurreDb;

CREATE TABLE categories(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(250) UNIQUE NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

ALTER TABLE categories
ADD INDEX index_categ (category_name);


CREATE TABLE foods(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(250) UNIQUE NOT NULL, 
    nova_group INT(1) NOT NULL,
    category_id INT(250) UNSIGNED NOT NULL,
    off_url VARCHAR(250),
    PRIMARY KEY (id)
)
ENGINE = INNODB;

ALTER TABLE foods
ADD INDEX index_foods_id (id),
ADD FOREIGN KEY (category_id) REFERENCES categories(id);


CREATE TABLE favorites(
    id INT(250) UNSIGNED NOT NULL AUTO_INCREMENT,
    foods_subs_id INT(250) UNSIGNED UNIQUE NOT NULL,
    foods_id INT(250) UNSIGNED UNIQUE NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

ALTER TABLE favorites
ADD FOREIGN KEY (foods_subs_id) REFERENCES foods(id),
ADD FOREIGN KEY (foods_id) REFERENCES foods(id);


CREATE TABLE stores(
    id INT(250) UNSIGNED NOT NULL AUTO_INCREMENT,
    stores_name VARCHAR (250) UNIQUE,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

ALTER TABLE stores
ADD INDEX index_stores (id);


CREATE TABLE foods_stores(
    id INT(250) UNSIGNED AUTO_INCREMENT,
    foods_id INT(250) UNSIGNED NULL,
    stores_id INT(250) UNSIGNED NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

ALTER TABLE foods_stores
ADD FOREIGN KEY (foods_id) REFERENCES foods(id),
ADD FOREIGN KEY (stores_id) REFERENCES stores(id);






-- commandes utiles 

DROP TABLE foods;
DROP TABLE categories;
DROP TABLE favorites;
DROP TABLE stores;
DROP TABLE foods_stores;

SELECT * FROM foods;
SELECT * FROM categories;
SELECT * FROM favorites;

ALTER TABLE foods
DROP column energy;



ALTER TABLE foods_stores MODIFY stores_id INT(250) UNSIGNED NULL;
