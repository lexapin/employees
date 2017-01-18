# -*- coding: utf-8 -*-
from application.modules.utilites import *
from application.modules.base import *
from datetime import date


app_module = {
  "base": {
    "name": "apps",
    "title": u"Модули приложения и доступ к ним",
    "table_caption": u"Модули приложения и доступ к ним",
    "form_caption": u"Разрешение на доступ роли к функциям модуля приложения",
    "function": table_view,
    "query": "SELECT role_view_association.id, view.caption, role.name FROM view INNER JOIN role_view_association INNER JOIN role WHERE role_id=role.id AND view_id=view.id ORDER BY view.id;"
  },
  "contextmenu_actions": ["edit", "delete",],
  "buttonsmenu_actions": ["add",],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": "INSERT INTO role_view_association (view_id, role_id) VALUES (%s, %s);",
      "attrs": ["view", "role"],
      "disabled": ["_id"]
    },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": "SELECT id, view_id, role_id FROM role_view_association WHERE id=%s;",
      "set_query": "UPDATE role_view_association SET view_id=%s, role_id=%s WHERE id = %s;",
      "attrs": ["view", "role", "_id"],
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
    "view": {
      "position": 1,
      "caption": u"Модуль приложения",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": list,
      "values_query": "SELECT id, caption FROM view;",
    },
    "role": {
      "position": 2,
      "caption": u"Идентификатор роли",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": list,
      "values_query": "SELECT id, name FROM role;",
    },
  },
}