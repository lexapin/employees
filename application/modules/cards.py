# -*- coding: utf-8 -*-
from flask import render_template
from config import get_db

def tuple_to_list(tuple_data):
  return [list(tuple_row) for tuple_row in tuple_data]

def get_cards():
  cursor = get_db().cursor()
  SQL = """
  SELECT
  employee.first_name, employee.last_name, card.personnel_number
  FROM employee
  INNER JOIN card
  WHERE employee_id = employee.id;
  """
  cursor.execute(SQL)
  data = cursor.fetchall()
  cursor.close()
  data = tuple_to_list(data)
  for i, row in enumerate(data):
    data[i][0] = row[0].decode("utf-8")
  return render_template("cards.html", title = u"Личные карточки учета кадров", cards = data)

def get_card(card_id):
  card = None
  return card

def create_card(data):
  return True

def update_card(card_id, data):
  return True

def delete_card(card_id):
  return True

def employees():
  cursor = get_db().cursor()
  SQL = """
  SELECT
  id, first_name, last_name
  FROM employee;
  """
  cursor.execute(SQL)
  data = cursor.fetchall()
  cursor.close()
  return render_template("table.html",
                  title = u"Сотрудники предприятия (базовая таблица)",
                  data = data, 
                  header = [u"#", u"Имя", u"Фамилия"]
                  )


"""
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `first_name` varchar(20),
  `last_name` varchar(20)
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
        REFERENCES employee(id)
);

insert into employee (first_name, last_name) values ("Алексей", "Фомин");
insert into card (
  employee_id,
  personnel_number,
  nature_of_work,
  type_of_work,
  date_of_birth,
  place_of_birth,
  education,
  foreign_language
) values(
  1,
  "1320",
  "офис",
  "инженер",
  508118400,
  "Чебоксары",
  "ЧГУ им.И.Н.Ульянова(2010)",
  "английский"
);
insert into employee (first_name, last_name) values ("Михаил", "Инюшкин");
insert into card (
  employee_id,
  personnel_number,
  nature_of_work,
  type_of_work,
  date_of_birth,
  place_of_birth,
  education,
  foreign_language
) values(
  2,
  "1800",
  "офис",
  "инженер-программист",
  609984000,
  "Чебоксары",
  "ЧГУ им.И.Н.Ульянова(2012)",
  "английский"
);

"""