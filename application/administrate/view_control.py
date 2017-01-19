# -*- coding: utf-8 -*-
from application.modules.utilites import *
from flask import redirect, url_for, flash, request
from flask.ext.login import current_user
from functools import wraps

def registrate_view(module):
  name = module["base"]["name"]
  caption = module["base"]["title"]
  registrate_view_query = """
    INSERT INTO view (name, caption)
    SELECT * FROM (SELECT "%s" AS name, "%s" AS caption) AS tmp
    WHERE NOT EXISTS (
    SELECT name
    FROM view
    WHERE view.name = tmp.name
    ) LIMIT 1;
    """
  response_data = set_data_to_db(registrate_view_query%(name, caption))
  if response_data:
    append_view_to_admin_role_query = "INSERT INTO role_view_association (role_id, view_id) values (1, %s);"%(response_data,)
    response_data = set_data_to_db(append_view_to_admin_role_query)
  return True


get_access_query = """
SELECT user.id
FROM user
INNER JOIN role
INNER JOIN role_view_association
INNER JOIN view
WHERE user.id = %s AND user.role_id = role.id AND role.id = role_view_association.role_id AND view_id = view.id AND view.name = '%s';
"""

def check_module_access(func):
  @wraps(func)
  def decorated_view(*args, **kwargs):
    view_name = func.__name__
    _id = current_user.get_id()
    access_OK = get_data_from_db(get_access_query%(_id, view_name))
    if access_OK:
      return func(*args, **kwargs)
    else:
      return redirect(url_for("closed"))
  return decorated_view
