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
      "caption": module["actions"][action_name],
    } for action_name in module["contextmenu_actions"]],
  }
  return context_menu

def create_buttons_menu(module):
  buttons_menu = {
    "actions": [{
      "name": action_name,
      "caption": module["actions"][action_name],
    } for action_name in module["buttonsmenu_actions"]],
  }
  return buttons_menu

def create_table_header(module):
  return [attr["caption"] for attr in sorted(module["attributes"].values(), key = lambda attr: attr["position"])]