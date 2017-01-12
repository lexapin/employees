# -*- coding: utf-8 -*-
from config import get_db
import datetime


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
  data = cursor.lastrowid
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


def create_form_items(module, view = None, values = None, disabled = []):
  if view is None: view = create_view(module)
  if values is not None and len(values) == len(view):
    for item, value in enumerate(values):
      view[item]["value"] = value
  form_fields = [create_input_field(item) for item in view]
  for field in form_fields:
    if field["name"] in disabled: field.update({"disabled": True, "hidden": True})
  return form_fields


def create_view(module):
  return [set_field(attr) for attr in sorted(module["attributes"].items(), key = lambda attr: attr[1]["position"])]


def set_field(attr):
  return dict(
      name = attr[0],
      caption = attr[1]["caption"],
      type = attr[1]["type"],
      activity = dict(
          readonly = False,
          hidden = False,
        ),
    )


def create_input_field(item):
  field = {}
  field["id"] = item["name"]
  field["name"] = item["name"]
  field["placeholder"] = item["caption"]
  field["type"] = type_table[item["type"].__name__]
  if "activity" in item: field.update({
    "readonly": item["activity"]["readonly"],
    "hidden": item["activity"]["hidden"],
    })
  else: field.update({"readonly": False, "hidden": False,})
  if "value" in item: field["value"] = item["value"]
  return field


def get_date(value):
  date = datetime.datetime.fromtimestamp(value)
  return u"-".join(["%02d"%value for value in [date.year, date.month, date.day]])


type_table = {
  int.__name__: "text",
  basestring.__name__: "text",
  datetime.date.__name__: "date"
}