# -*- coding: utf-8 -*-
from config import get_db


def tuple_to_list(tuple_data):
  return [list(tuple_row) for tuple_row in tuple_data]


def get_data_from_db(SQL_QUERY):
  cursor = get_db().cursor()
  cursor.execute(SQL_QUERY)
  data = cursor.fetchall()
  cursor.close()
  return data


def set_data_to_db(SQL_QUERY):
  db = get_db()
  cursor = db.cursor()
  cursor.execute(SQL_QUERY)
  db.commit()
  data = cursor.fetchone()
  cursor.close()
  return data


def create_context_menu(module):
  context_menu = {
    "actions": [{
      "name": action_name,
      "caption": module["actions"][action_name]["caption"],
    } for action_name in module["contextmenu_actions"]],
  }
  return context_menu


def create_buttons_menu(module):
  buttons_menu = {
    "actions": [{
      "name": action_name,
      "caption": module["actions"][action_name]["caption"],
    } for action_name in module["buttonsmenu_actions"]],
  }
  return buttons_menu


def create_table_header(module):
  return [attr["caption"] for attr in sorted(module["attributes"].values(), key = lambda attr: attr["position"])]


def create_decode_table(module):
  return {
    attr["position"]: attr.get("decode_function", lambda value: value) for attr in module["attributes"].values()
  }


# employee = [
#         dict(
#           type = "text",
#           id = "_id",
#           name = "_id",
#           placeholder = u"#",
#           value = employee[0],
#           readonly = True,
#           ),
#         dict(
#           type = "text",
#           id = "first_name",
#           name = "first_name",
#           placeholder = u"Имя",
#           value = employee[1],
#           readonly = False,
#           ),
#         dict(
#           type = "text",
#           id = "last_name",
#           name = "last_name",
#           placeholder = u"Фамилия",
#           value = employee[2],
#           readonly = False,
#           ),
#       ]
def create_form_items(module, view = None, values = None):
  if view is None: create_view(module)


def create_view(module):
  # [{item: form_item, attr: module_attr, caption}, ... ]
  return [{} for attr in sorted(module["attributes"].values(), key = lambda attr: attr["position"])]
