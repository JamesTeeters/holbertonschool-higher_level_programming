-- create a User with all permissions
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';