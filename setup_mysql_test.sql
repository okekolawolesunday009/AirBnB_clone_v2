-- Create the database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Use the previous database
USE hbnb_test_db;
-- Create the specific user to this database
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Give the priviliges to this database to the user
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

