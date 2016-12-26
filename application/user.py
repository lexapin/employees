# -*- coding: utf-8 -*-
from flask.ext.login import UserMixin
from config import get_db

class User(object):
  __slots__ = 'id', 'username', 'password', 'buttons'

  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.buttons = [{"func": "upload", "name": u"Загрузить файл"}, {"func": "logout", "name": u"Выйти"}]

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
    return self.username

  @classmethod
  def get(cls, _id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT username, password FROM user WHERE id = %s;", (_id,))
    data = cursor.fetchone()
    cursor.close()
    return User(data[0], data[1]) if data else None