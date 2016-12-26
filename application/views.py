# -*- coding: utf-8 -*-
from application import app, login_required_when_anonymous
from flask import render_template, flash, redirect, make_response, request, url_for, \
          send_file, g

# from database.deduplication import *
from application.user import User
from flask.ext.login import login_user, logout_user, current_user
import StringIO


@app.before_request
def before_request():
  g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html', title = u"Вход")
  f = File()
  cursor = f.db.cursor()
  username = request.form['username']
  password = request.form['password']
  if username != "guest":
    count = cursor.execute("SELECT username, password FROM users WHERE username = %s AND password = %s", (username, password))
    if not count:
      flash(u"Имя пользователя или пароль введены неправильно")
      return redirect(url_for('login'))
    registered_user = cursor.fetchone()
    print registered_user, "1"*10
    login_user(User(registered_user[0], registered_user[1]))

  flash(u"Вход выполнен, %s"%current_user)
  return redirect(request.args.get('next') or url_for('user'))


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))


@app.route('/')
def index():
  # f = File()
  # cursor = f.db.cursor()
  # cursor.execute("SELECT id, name, size FROM file;")
  # data = cursor.fetchall()
  # cursor.close()
  # return render_template("index.html", title = u"Файловое хранилище. Бета-версия. Версия 2.0", files = data)
  try:
    from config import admin
  except:
    user = "not imported"
  else:
    user = "password %s"%admin
  return str(current_user)+user