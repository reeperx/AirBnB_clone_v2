-- This script creates a new user 'hbnb_test' with the password 'hbnb_test_pwd' if it doesn't already exist
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';

-- This creates a new database 'hbnb_test_db' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- This grants all privileges on the 'hbnb_test_db' database to the 'hbnb_test' user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;

-- This grants the 'SELECT' privilege on the 'performance_schema' database to the 'hbnb_test' user
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
