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
  if current_user.is_anonymous(): return redirect(url_for('login'))
  return redirect(url_for('employees'))

from application.modules.cards import employee_module, card_module

@app.route('/employees', methods=['GET'])
@app.route('/employees/<action>', methods=['GET', 'POST'])
@app.route('/employees/<action>/<_id>', methods=['GET', 'POST'])
def employees(action = None, _id = None):
  if _id is None and action is None: return employee_module["base"]["function"](employee_module)
  form = employee_module["actions"][action]["function"]
  if request.method == 'GET': return form(employee_module, action, _id)
  if request.method == 'POST': return form(employee_module, action, _id, request.form)


@app.route('/cards', methods=['GET'])
@app.route('/cards/<action>', methods=['GET', 'POST'])
@app.route('/cards/<action>/<_id>', methods=['GET', 'POST'])
def cards(action = None, _id = None):
  if _id is None and action is None: return card_module["base"]["function"](card_module)
  form = card_module["actions"][action]["function"]
  if request.method == 'GET': return form(card_module, action, _id)
  if request.method == 'POST': return form(card_module, action, _id, request.form)


from application.modules.finance import finance_module, finance_report_module

@app.route('/report/finance', methods=['GET'])
def halfyearreport():
  return finance_report_module["base"]["function"](finance_report_module)

@app.route('/finance', methods=['GET'])
@app.route('/finance/<action>', methods=['GET', 'POST'])
@app.route('/finance/<action>/<_id>', methods=['GET', 'POST'])
def cards(action = None, _id = None):
  if _id is None and action is None: return finance_module["base"]["function"](finance_module)
  form = finance_module["actions"][action]["function"]
  if request.method == 'GET': return form(finance_module, action, _id)
  if request.method == 'POST': return form(finance_module, action, _id, request.form)