# -*- coding: utf-8 -*-
from flask.ext.login import UserMixin
from config import get_db

categories = [
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

class User(object):
  __slots__ = 'id', 'username', 'password', 'buttons'

  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.buttons =  [
                      {"type": "button", "name": u"Выйти", "func": "logout"},
                    ]

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM user WHERE username = %s", (self.username,))
    self.id = cursor.fetchone()[0]
    cursor.close()
    return unicode(self.id)

  def __repr__(self):
    return self.username.decode("utf-8")

  @classmethod
  def get(cls, _id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT username, password FROM user WHERE id = %s;", (_id,))
    data = cursor.fetchone()
    cursor.close()
    return User(data[0], data[1]) if data else None