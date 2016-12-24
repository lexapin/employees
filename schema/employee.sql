DROP TABLE IF EXISTS employee_month_pay_association;
DROP TABLE IF EXISTS employee_children_association;
DROP TABLE IF EXISTS employee_position_association;
DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS month_pay;
DROP TABLE IF EXISTS child;
DROP TABLE IF EXISTS position;

CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `first_name` varchar(20),
  `last_name` varchar(20),
);

CREATE TABLE `card` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `employee_id` int NOT NULL,
  `personnel_number` varchar(20),
  `nature of work`   varchar(20),
  `type_of_work`     varchar(20),
  `date_of_birth`    int(11),
  `place_of_birth`   varchar(20),
  `education`        varchar(20),
  `foreign_language` varchar(20),
  FOREIGN KEY (employee_id)
        REFERENCES employee(id),
);

CREATE TABLE `month_pay` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `month` int NOT NULL,
  `year` int NOT NULL,
  `salary` int NOT NULL,
  `bonus` int NOT NULL,
);

CREATE TABLE `employee_month_pay_association` (
  `id` int NOT NULL primary key AUTO_INCREMENT,
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
  `date_of_birth` int(11),
);

CREATE TABLE 'employee_children_association' (
  `id` int NOT NULL primary key AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `child_id` int DEFAULT NULL,
  FOREIGN KEY (employee_id)
        REFERENCES employee(id),
  FOREIGN KEY (child_id)
        REFERENCES child(id)
);

CREATE TABLE `position` (
  `id` int NOT NULL primary key AUTO_INCREMENT,
  `post_name` varchar(30),
  `assign_date` int,
);

CREATE TABLE 'employee_position_association' (
  `id` int NOT NULL primary key AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `position_id` int DEFAULT NULL,
  FOREIGN KEY (employee_id)
        REFERENCES employee(id),
  FOREIGN KEY (position_id)
        REFERENCES position(id)
);
