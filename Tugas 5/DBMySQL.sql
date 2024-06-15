CREATE DATABASE fastapi;
CREATE TABLE items (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    description varchar(255),
    PRIMARY KEY (id)
);