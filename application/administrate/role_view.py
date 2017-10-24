# -*- coding: utf-8 -*-
from application.modules.utilites import *
from application.modules.base import *
from datetime import date


role_module = {
  "base": {
    "name": "roles",
    "title": u"Роли в приложении",
    "table_caption": u"Роли в приложении",
    "form_caption": u"Роль",
    "function": table_view,
    "query": "SELECT id, name FROM role;"
  },
  "contextmenu_actions": ["edit", "delete",],
  "buttonsmenu_actions": ["add",],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": "INSERT INTO role (name) VALUES ('%s');",
      "attrs": ["name"],
      "disabled": ["_id"]
    },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": "SELECT id, name FROM role WHERE id=%s;",
      "set_query": "UPDATE role SET name='%s' WHERE id = %s;",
      "attrs": ["name", "_id"],
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
    "name": {
      "position": 1,
      "caption": u"Идентификатор роли",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
  },
}