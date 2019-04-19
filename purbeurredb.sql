CREATE DATABASE PurBeurreDb;

CREATE TABLE categories(
    id SMALLINT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(250) UNIQUE NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

ALTER TABLE categories
ADD INDEX index_categ (category_name);

CREATE TABLE foods(
    id SMALLINT NOT NULL AUTO_INCREMENT,
    Product_name VARCHAR(250) NOT NULL,
    nova_group INT(1) NOT NULL,
    category_name VARCHAR(250) NOT NULL,
    countries_tags TEXT(1000) NOT NULL,
    stores_tags TEXT(1000),
    off_url TEXT(1000),
    PRIMARY KEY (id)
)
ENGINE = INNODB;

ALTER TABLE foods
ADD FOREIGN KEY (category_name) REFERENCES categories(category_name);

CREATE TABLE favorites(
    id SMALLINT NOT NULL AUTO_INCREMENT,
    Product_name VARCHAR(250) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

-- commandes utiles 

DROP TABLE foods;
DROP TABLE categories;
DROP TABLE favorites;

SELECT * FROM foods;
SELECT * FROM categories;
SELECT * FROM favorites;

ALTER TABLE foods
DROP column energy;



