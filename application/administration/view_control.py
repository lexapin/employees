# -*- coding: utf-8 -*-
from application.modules.utilites import *

def registrate_view(module):
  name = module["base"]["name"]
  caption = module["base"]["title"]
  load_view_query = "INSERT INTO view (name, caption)"
  return True

place_module = {
  "base": {
    "name": "places",
    "title": u"Должности сотрудников",
    "table_caption": u"Должности сотрудников",
    "form_caption": u"Информация о должности сотрудника",
    "function": table_view,
    "query": place_query,
  },}

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