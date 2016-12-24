# -*- coding: utf-8 -*-
import os

script_file = None
if __name__ == "__main__":
	script_file = open(os.getcwd() + "/employee.sql", "r")
else:
	script_file = open(os.getcwd() + "/database/employee.sql", "r")
script = script_file.read()
script_file.close()

conf = {
	"host": "mysql.server",
	"username": "robot4",
	"password": "12345",
	"database": "robot4$employee"
}

import MySQLdb as mysql
db = mysql.connect(conf["host"], conf["username"], conf["password"], conf["database"])
# db.set_character_set('utf8')

cursor = db.cursor()
cursor.execute(script)
cursor.close()