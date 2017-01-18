# -*- coding: utf-8 -*-
from application.modules.utilites import *

def registrate_view(module):
  name = module["base"]["name"]
  caption = module["base"]["title"]
  registrate_view_query = "INSERT INTO view (name, caption) VALUES %s, %s;"
  response_data = set_data_to_db(registrate_view_query%(name, caption))
  if response_data:
    append_view_to_admin_role_query = "INSERT INTO role_view_association (role_id, view_id) values (1, %s);"%(response_data,)
    response_data = set_data_to_db(append_view_to_admin_role_query)
  return True


"""
INSERT INTO view (name, caption)
SELECT * FROM (SELECT %s AS name, %s AS caption) AS tmp
WHERE NOT EXISTS (
SELECT name
FROM view
WHERE view.name = tmp.name
) LIMIT 1;
"""


# sample
"""
INSERT INTO view (name, caption)
SELECT * FROM (SELECT "places" AS name, "Должности сотрудников" AS caption) AS tmp
WHERE NOT EXISTS (
SELECT name
FROM view
WHERE view.name = tmp.name
) LIMIT 1;
"""

"""
INSERT INTO role (name) values ("Администратор");
"""

"""
INSERT INTO role_view_association (role_id, view_id) values (1, 1);
"""

"""
SELECT role.name, view.caption
FROM role
INNER JOIN role_view_association
INNER JOIN view
WHERE role_id=role.id AND view_id=view.id;
"""