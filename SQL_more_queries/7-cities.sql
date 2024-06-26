-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database hbtn_0d_usa 
USE hbtn_0d_usa;

-- create table states
CREATE TABLE if NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
)