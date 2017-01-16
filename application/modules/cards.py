# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash
from utilites import *
from base import *
from datetime import date


def add_employee_card(data):
  data = tuple(data)
  set_data_to_db("INSERT INTO card (employee_id) VALUES (%s);"%(data))
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
      "trigger": add_employee_card,
      "disabled": ["_id"]
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
  "buttonsmenu_actions": [],
  "actions": {
    # "add": {
    #   "caption": u"Добавить",
    #   "function": update_function,
    #   "set_query": "INSERT INTO employee (first_name, last_name) VALUES ('%s', '%s');",
    #   "attrs": ["first_name", "last_name"],
    # },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": "SELECT employee_id, first_name, last_name, personnel_number, nature_of_work, type_of_work, date_of_birth, place_of_birth, education, foreign_language FROM employee JOIN card WHERE employee.id=employee_id and employee_id=%s;",
      "set_query": "UPDATE card SET personnel_number = '%s', nature_of_work = '%s', type_of_work = '%s', date_of_birth = '%s', place_of_birth = '%s', education = '%s', foreign_language = '%s' WHERE employee_id = %s;",
      "attrs": ["personnel_number", "nature_of_work", "type_of_work", "date_of_birth", "place_of_birth", "education", "foreign_language", "_id"],
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
      "decode_function": lambda value: get_date(value),
      "encode_function": lambda value: set_date(value),
      "type": date,
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