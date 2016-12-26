# -*- coding: utf-8 -*-
import MySQLdb as mysql

CSRF_ENABLED = True
SECRET_KEY = 'secret-key-for-emloyees'

admin = "password"


def get_db():
  conf = {
    "host": "robot4.mysql.pythonanywhere-services.com",
    "username": "robot4",
    "password": "12345",
    "database": "robot4$employee"
  }
  return mysql.connect(conf["host"], conf["username"], conf["password"], conf["database"])