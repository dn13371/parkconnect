BEGIN TRANSACTION;
DELETE FROM users;
INSERT INTO users(UserName, Mail, Password) VALUES ("admin", "admin@mail.de", "admin");
COMMIT;