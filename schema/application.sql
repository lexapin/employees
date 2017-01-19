DROP TABLE IF EXISTS role_view_association;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS role;
DROP TABLE IF EXISTS view;

CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `name` varchar(20) unique
);

CREATE TABLE `view` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `name` varchar(20) unique,
  `caption` varchar(90)
);

CREATE TABLE `role_view_association` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `role_id` int DEFAULT NULL,
  `view_id` int DEFAULT NULL,
  FOREIGN KEY (role_id)
        REFERENCES role(id),
  FOREIGN KEY (view_id)
        REFERENCES view(id)
);

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `username` varchar(20) unique,
  `password` varchar(20),
  `role_id`  int DEFAULT NULL,
  FOREIGN KEY (role_id)
        REFERENCES role(id)
);
