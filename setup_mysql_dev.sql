-- Creates a database named hbnb_dev_db if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates a user named 'hbnb_dev' with the password 'hbnb_dev_pwd' if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants the 'hbnb_dev' user SELECT privileges on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Grants the 'hbnb_dev' user ALL privileges on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
