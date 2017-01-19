# -*- coding: utf-8 -*-
from flask.ext.login import UserMixin
from application.modules.utilites import *

class User(object):
  __slots__ = 'id', 'username', 'password', 'buttons'

  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.user_auth()

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    username = self.username.decode("utf-8")
    self.id = get_data_from_db("SELECT id FROM user WHERE username='%s';"%(username))[0][0]
    return unicode(self.id)

  def __repr__(self):
    return self.username.decode("utf-8")

  def user_auth(self):
    user_id = self.get_id()
    self.buttons =  [
                      {"type": "button", "name": u"Выйти", "func": "logout"},
                    ]
    pass

  @classmethod
  def get(cls, _id):
    data = get_data_from_db("SELECT username, password FROM user WHERE id = %s;"%(_id,))
    return User(data[0][0], data[0][1]) if data else None


CATEGORIES = [
  {
    "type": "menu",
    "name": u"Общая информация",
    "buttons":
        [
          "employees",
          "cards",
        ]
  },
  {
    "type": "menu",
    "name": u"Зарплата",
    "buttons":
        [
          "finance",
          "halfyearreport",
        ]
  },
  {
    "type": "menu",
    "name": u"Профсоюз",
    "buttons":
        [
          "children",
          "places",
        ]
  },
  {
    "type": "menu",
    "name": u"Администрирование",
    "buttons":
        [
          "roles",
          "users",
          "apps",
        ]
  },
]

GET_USER_MODULES_QUERY = """
SELECT
"""