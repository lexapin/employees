# -*- coding: utf-8 -*-
import os

script_file = None
if __name__ == "__main__":
	script_file = open(os.getcwd() + "/application.sql", "r")
else:
	script_file = open(os.getcwd() + "/database/application.sql", "r")
script = script_file.read()
script_file.close()

conf = {
	"host": "robot4.mysql.pythonanywhere-services.com",
	"username": "robot4",
	"password": "12345",
	"database": "robot4$employee"
}

import MySQLdb as mysql
db = mysql.connect(conf["host"], conf["username"], conf["password"], conf["database"])

cursor = db.cursor()
cursor.execute(script)
cursor.close()