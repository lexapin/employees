DROP TABLE IF EXISTS user
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `username` varchar(20) unique,
  `password` varchar(20),
   index(username)
);
INSERT INTO users (username, password) VALUES ("admin", "admin");