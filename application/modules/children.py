# -*- coding: utf-8 -*-
from base import *
from datetime import date


children_query = """
SELECT child_id, name, child.date_of_birth, CONCAT(first_name, " ", last_name)
FROM employee
INNER JOIN employee_children_association
INNER JOIN child
WHERE employee.id=employee_id AND child.id=child_id
ORDER BY employee_id;
"""

add_child_query = """
INSERT INTO child (name, date_of_birth) VALUES ('%s', %s);
"""

add_employee_children_association_query = """
INSERT INTO employee_children_association (child_id, employee_id) VALUES (%s, %s);
"""

def add_employee_children_association(data):
  data = tuple(data)
  set_data_to_db(add_employee_children_association_query%(data))
  return

get_form_to_update_child_info_query = """
SELECT child.id, name, date_of_birth, employee_id
FROM employee_children_association
INNER JOIN child 
WHERE child_id=%s AND child.id=child_id;
"""

edit_child_query = """
UPDATE child SET name='%s', date_of_birth=%s WHERE id = %s;
"""

children_module = {
  "base": {
    "name": "children",
    "title": u"Дети сотрудников",
    "table_caption": u"Дети сотрудников",
    "form_caption": u"Информация о ребенке сотрудника",
    "function": table_view,
    "query": children_query,
  },
  "contextmenu_actions": ["edit"],
  "buttonsmenu_actions": ["add"],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": add_child_query,
      "attrs": ["name", "date_of_birth"],
      "trigger": add_employee_children_association,
      "vars_to_trigger": ["employee"],
      "disabled": ["_id"],
    },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": get_form_to_update_child_info_query,
      "set_query": edit_child_query,
      "attrs": ["name", "date_of_birth", "_id"],
    },
  },
  "attributes": {
    "_id": {
      "position": 0,
      "caption": u"#",
      "type": int,
    },
    "name": {
      "position": 1,
      "caption": u"Имя",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "date_of_birth": {
      "position": 2,
      "caption": u"Дата рождения ребенка",
      "decode_function": lambda value: get_date(value),
      "encode_function": lambda value: set_date(value),
      "type": date,
    },
    "employee": {
      "position": 3,
      "caption": u"Имя, Фамилия сотрудника",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": list,
      "values_query": "SELECT id, CONCAT(first_name, ' ', last_name) FROM employee;",
    },
  },
}


children_report_module = {
  "base": {
    "name": "children15yearold",
    "title": u"Дети сотрудников не достигших 15 летнего возраста на 1 января следующего года",
    "table_caption": u"Дети сотрудников не достигших 15 летнего возраста на 1 января следующего года",
    "form_caption": u"Информация о ребенке сотрудника",
    "function": table_view,
    "query": children_query,
  },
  "contextmenu_actions": [],
  "buttonsmenu_actions": [],
  "actions": {},
  "attributes": {
    "_id": {
      "position": 0,
      "caption": u"#",
      "type": int,
    },
    "name": {
      "position": 1,
      "caption": u"Имя",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "date_of_birth": {
      "position": 2,
      "caption": u"Дата рождения ребенка",
      "decode_function": lambda value: get_date(value),
      "encode_function": lambda value: set_date(value),
      "type": date,
    },
    "employee": {
      "position": 3,
      "caption": u"Имя, Фамилия сотрудника",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": list,
      "values_query": "SELECT id, CONCAT(first_name, ' ', last_name) FROM employee;",
    },
  },
}


"""
INSERT INTO child (name, date_of_birth) VALUES ("Инюшкина Екатерина Михайловна", 1475625600);
INSERT INTO employee_children_association (employee_id, child_id) VALUES (2, 1);
"""