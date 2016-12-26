# -*- coding: utf-8 -*-
from application import app, login_required_when_anonymous
from flask import render_template, flash, redirect, make_response, request, url_for, \
          send_file, g

from application.user import User
from flask.ext.login import login_user, logout_user, current_user
import StringIO

from config import admin as admin_password
from config import get_db

@app.before_request
def before_request():
  g.user = current_user


def registration_failed_redirection():
  flash(u"Имя пользователя или пароль введены неправильно")
  return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html', title = u"Вход")
  username = request.form['username']
  password = request.form['password']
  db = get_db()
  cursor = db.cursor()
  count = cursor.execute("SELECT username, password FROM user WHERE username = %s AND password = %s", (username, password))
  if not count: return registration_failed_redirection()
  registered_user = cursor.fetchone()
  login_user(User(registered_user[0], registered_user[1]))

  flash(u"Вход выполнен, %s"%current_user)
  return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))


@app.route('/')
def index():
  # db = get_db()
  # cursor = db.cursor()
  # cursor.execute("SELECT id, name, size FROM file;")
  # data = cursor.fetchall()
  # cursor.close()
  # return render_template("index.html", title = u"Файловое хранилище. Бета-версия. Версия 2.0", files = data)
  if current_user.is_anonymous(): return redirect(url_for('login'))
  returned_string = "Hello, "+ current_user.username.encode('utf-8')
  return returned_string

from application.modules.cards import *
@app.route('/cards', methods=['GET', 'POST'])
def cards():
  if request.method == 'GET': return get_cards()