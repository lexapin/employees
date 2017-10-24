# -*- coding: utf-8 -*-
from base import *
from datetime import date

# place_name
# assign_date

place_query = """
SELECT place_id, CONCAT(first_name, " ", last_name), place_name, assign_date
FROM employee
INNER JOIN employee_place_association
INNER JOIN place
WHERE employee.id=employee_id AND place.id=place_id
ORDER BY employee_id;
"""

add_place_query = """
INSERT INTO place (place_name, assign_date) VALUES ('%s', %s);
"""

add_employee_place_association_query = """
INSERT INTO employee_place_association (place_id, employee_id) VALUES (%s, %s);
"""

def add_employee_place_association(data):
  data = tuple(data)
  set_data_to_db(add_employee_place_association_query%(data))
  return

get_form_to_update_place_info_query = """
SELECT place.id, employee_id, place_name, assign_date
FROM employee_place_association
INNER JOIN place 
WHERE place_id=%s AND place.id=place_id;
"""

edit_place_query = """
UPDATE place SET place_name='%s', assign_date=%s WHERE id = %s;
"""

place_module = {
  "base": {
    "name": "places",
    "title": u"Должности сотрудников",
    "table_caption": u"Должности сотрудников",
    "form_caption": u"Информация о должности сотрудника",
    "function": table_view,
    "query": place_query,
  },
  "contextmenu_actions": ["edit"],
  "buttonsmenu_actions": ["add"],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": add_place_query,
      "attrs": ["place_name", "assign_date"],
      "trigger": add_employee_place_association,
      "vars_to_trigger": ["employee"],
      "disabled": ["_id"],
    },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": get_form_to_update_place_info_query,
      "set_query": edit_place_query,
      "attrs": ["place_name", "assign_date", "_id"],
    },
  },
  "attributes": {
    "_id": {
      "position": 0,
      "caption": u"#",
      "type": int,
    },
    "employee": {
      "position": 1,
      "caption": u"Имя, Фамилия",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": list,
      "values_query": "SELECT id, CONCAT(first_name, ' ', last_name) FROM employee;",
    },
    "place_name": {
      "position": 2,
      "caption": u"Текущая должность",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "assign_date": {
      "position": 3,
      "caption": u"Дата назначения",
      "decode_function": lambda value: get_date(value),
      "encode_function": lambda value: set_date(value),
      "type": date,
    },
  },
}


"""
INSERT INTO place (place_name, assign_date) VALUES ("Инженер-программист 3-ей кат.", 1475625600);
INSERT INTO employee_place_association (employee_id, place_id) VALUES (2, 1);
"""