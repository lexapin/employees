# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash
from utilites import *
from base import *

def add_employee_card(employee_id):
  set_data_to_db("INSERT INTO card (employee_id) VALUES (%s);"%employee_id)
  return

employee_module = {
  "base": {
    "name": "employees",
    "title": u"Сотрудники предприятия",
    "table_caption": u"Сотрудники предприятия (базовая таблица)",
    "form_caption": u"Имя, Фамилия сотрудника",
    "function": table_view,
    "query": "SELECT id, first_name, last_name FROM employee;"
  },
  "contextmenu_actions": ["edit", "delete",],
  "buttonsmenu_actions": ["add",],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": "INSERT INTO employee (first_name, last_name) VALUES ('%s', '%s');",
      "attrs": ["first_name", "last_name"],
      "trigger": add_employee_card
    },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": "SELECT id, first_name, last_name FROM employee WHERE id=%s;",
      "set_query": "UPDATE employee SET first_name='%s', last_name='%s' WHERE id = %s;",
      "attrs": ["first_name", "last_name", "_id"],
    },
    "delete": {
      "caption": u"Удалить",
      "function": delete_function,
      "set_query": "",
      "attrs": ["_id"],
    },
  },
  "attributes": {
    "_id": {
      "position": 0,
      "caption": u"#",
      "type": int,
    },
    "first_name": {
      "position": 1,
      "caption": u"Имя",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "last_name": {
      "position": 2,
      "caption": u"Фамилия",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
  },
}

card_module = {
  "base": {
    "name": "cards",
    "title": u"Личные карточки учета кадров предприятия",
    "table_caption": u"Личные карточки учета кадров предприятия",
    "form_caption": u"Имя, Фамилия сотрудника",
    "function": table_view,
    "query": "SELECT employee_id, first_name, last_name, personnel_number, nature_of_work, type_of_work, date_of_birth, place_of_birth, education, foreign_language FROM employee JOIN card WHERE employee.id=employee_id;"
  },
  "contextmenu_actions": ["edit", "delete",],
  "buttonsmenu_actions": ["add",],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": "INSERT INTO employee (first_name, last_name) VALUES ('%s', '%s');",
      "attrs": ["first_name", "last_name"],
    },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": "SELECT id, first_name, last_name FROM employee WHERE id=%s;",
      "set_query": "UPDATE employee SET first_name='%s', last_name='%s' WHERE id = %s;",
      "attrs": ["first_name", "last_name", "_id"],
    },
    "delete": {
      "caption": u"Удалить",
      "function": delete_function,
      "set_query": "",
      "attrs": ["_id"],
    },
  },
  "attributes": {
    "_id": {
      "position": 0,
      "caption": u"#",
      "type": int,
    },
    "first_name": {
      "position": 1,
      "caption": u"Имя",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "last_name": {
      "position": 2,
      "caption": u"Фамилия",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "personnel_number": {
      "position": 3,
      "caption": u"Табельный номер",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "nature_of_work": {
      "position": 4,
      "caption": u"Рабочее место",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "type_of_work": {
      "position": 5,
      "caption": u"Профессия",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "date_of_birth": {
      "position": 6,
      "caption": u"Дата рождения",
      "decode_function": lambda value: int(value),
      "type": basestring,
    },
    "place_of_birth": {
      "position": 7,
      "caption": u"Место рождения",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "education": {
      "position": 8,
      "caption": u"Образование",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "foreign_language": {
      "position": 9,
      "caption": u"Основной иностранный язык",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
  },
}

# def employee_form(module, action, _id = None, data = None):
#   GET_QUERY = module["actions"][action]["get_query"]
#   SET_QUERY = module["actions"][action]["set_query"]
#   if data is None:
#     db_items = None if _id is None else get_data_from_db(GET_QUERY%(_id,))[0]
#     disabled = ["_id"] if _id is None else []
#     return render_template("form.html", 
#                             items = create_form_items(employee_module, view = None, values = db_items, disabled = disabled),
#                             base = employee_module["base"],
#                             decode = create_decode_table(employee_module),
#                           )
#   else:
#     if (_id is not None) and ( (not get_data_from_db(GET_QUERY%(_id,)) ) or ( _id != data["_id"]) ):
#       flash(u"Данные о сотруднике введены некорректно!!!")
#       return redirect(url_for('index'))
#     attrs = [data[attr] for attr in module["actions"][action]["attrs"]]
#     try:
#       set_data_to_db(SET_QUERY%(*attrs))
#     except Exception as err:
#       flash(u"Ошибка в процессе записи в базу данных новых значений")
#       flash(str(err))
#     else:
#       flash(u"Данные успешно изменены")
#     return redirect(url_for('index'))



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