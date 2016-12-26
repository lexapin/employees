DROP TABLE IF EXISTS employee_month_pay_association;
DROP TABLE IF EXISTS employee_children_association;
DROP TABLE IF EXISTS employee_place_association;
DROP TABLE IF EXISTS child;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS month_pay;
DROP TABLE IF EXISTS employee;

CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `first_name` varchar(20),
  `last_name` varchar(20)
);

CREATE TABLE `card` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `personnel_number` varchar(20),
  `nature_of_work`   varchar(20),
  `type_of_work`     varchar(20),
  `date_of_birth`    int(11),
  `place_of_birth`   varchar(20),
  `education`        varchar(20),
  `foreign_language` varchar(20),
  `employee_id` int NOT NULL,
  FOREIGN KEY (employee_id)
        REFERENCES employee(id)
);

CREATE TABLE `month_pay` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `month` int NOT NULL,
  `year` int NOT NULL,
  `salary` int NOT NULL,
  `bonus` int NOT NULL
);

CREATE TABLE `employee_month_pay_association` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `employee_id` int NOT NULL,
  `month_pay_id` int NOT NULL,
  FOREIGN KEY (employee_id)
        REFERENCES employee(id),
  FOREIGN KEY (month_pay_id)
        REFERENCES month_pay(id)
);

CREATE TABLE `child` (
  `id` int NOT NULL primary key AUTO_INCREMENT,
  `name` varchar(100),
  `date_of_birth` int(11)
);

CREATE TABLE `employee_children_association` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `employee_id` int DEFAULT NULL,
  `child_id` int DEFAULT NULL,
  FOREIGN KEY (employee_id)
        REFERENCES employee(id),
  FOREIGN KEY (child_id)
        REFERENCES child(id)
);

CREATE TABLE `place` (
  `id` int NOT NULL primary key AUTO_INCREMENT,
  `place_name` varchar(30),
  `assign_date` int(11)
);

CREATE TABLE `employee_place_association` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `employee_id` int(11) DEFAULT NULL,
  `place_id` int(11) DEFAULT NULL,
  FOREIGN KEY (employee_id)
        REFERENCES employee(id),
  FOREIGN KEY (place_id)
        REFERENCES place(id)
);
