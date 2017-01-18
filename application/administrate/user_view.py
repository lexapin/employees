# -*- coding: utf-8 -*-
from application.modules.utilites import *
from application.modules.base import *
from datetime import date


user_module = {
  "base": {
    "name": "users",
    "title": u"Пользователи приложения",
    "table_caption": u"Пользователи приложения",
    "form_caption": u"Пользователь и его роль в приложении",
    "function": table_view,
    "query": "SELECT user.id, username, role.name FROM user INNER JOIN role WHERE role_id=role.id ORDER BY user.id;"
  },
  "contextmenu_actions": ["edit", "delete",],
  "buttonsmenu_actions": ["add",],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": "INSERT INTO user (username, role_id) VALUES ('%s', %s);",
      "attrs": ["username", "rolename"],
      "disabled": ["_id"]
    },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": "SELECT id, username, role_id FROM user WHERE id=%s;",
      "set_query": "UPDATE user SET username='%s', role_id=%s WHERE id = %s;",
      "attrs": ["username", "rolename", "_id"],
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
    "username": {
      "position": 1,
      "caption": u"Идентификатор пользователя",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "rolename": {
      "position": 2,
      "caption": u"Идентификатор роли",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": list,
      "values_query": "SELECT id, name FROM role;",
    },
  },
}