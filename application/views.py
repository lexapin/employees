# -*- coding: utf-8 -*-
from application import app, login_required_when_anonymous
from flask import render_template, flash, redirect, make_response, request, url_for, \
          send_file, g, Response

from application.user import User
from flask.ext.login import login_user, logout_user, current_user
import StringIO

from config import admin as admin_password
from config import get_db

from application.administrate.view_control import registrate_view, check_module_access
# вьюхи панели администрирования
from application.administrate.role_view import role_module
from application.administrate.user_view import user_module
from application.administrate.module_view import app_module

# вьюхи приложения
from application.modules.cards import employee_module, card_module
from application.modules.finance import finance_module, finance_report_module
from application.modules.children import children_module, children_report_module
from application.modules.career import place_module

from time import sleep

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))


@app.route('/')
def index():
  if current_user.is_anonymous(): return redirect(url_for('login'))
  return redirect(url_for('employees'))


@app.route('/closed')
def closed():
  return render_template("closed.html")


@app.route('/form')
def form():
  return render_template("modalforms.html")


class Queue:
  def __init__(self, limit = float("inf")):
    self.__storage = []
    self.__limit = limit
    self.__index = 0
  
  def isEmpty(self):
    return self.__index == 0
  
  def push(self, data):
    self.__index+=1
    self.__storage.append(data)
    if self.__index == self.__limit: self.pop()
  
  def pop(self):
    if not self.isEmpty():
      self.__index-=1
      return self.__storage.pop(0)
    return None

  def __repr__(self):
    return str(self.__storage)

global image_queue
image_queue = Queue()

@app.route('/stream/upload', methods=['POST'])
def upload():
  global image_queue
  file = request.files.get("file", None)
  image_queue.push(file.read())
  # Save uploaded images to server storage
  size = 0
  # with open("/".join(["/home/robot4/uploaded_files", file.filename]), "wb") as server_file:
  #   server_file.write(file.read())
  #   size = server_file.tell()
  return file.filename+str(size)

@app.route('/stream/view', methods=['GET'])
def page():
  return render_template('stream.html')

@app.route('/stream/data', methods=['GET'])
def view_stream():
  def image_generator(queue):
    frame = queue.pop()
    if frame is None:
      pass
    sleep(1)
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
  global image_queue
  return Response(image_generator(image_queue),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stream/queue', methods=['GET'])
def queue():
  global image_queue
  return str(image_queue.isEmpty())

# Основная часть приложения
class TableView(object):
  """docstring for TableView"""
  def __init__(self, app, module):
    super(TableView, self).__init__()
    self.__module__ = module
    self.__name__ = self.__module__["base"]["name"]
    app.add_url_rule('/%s'%self.__name__, view_func = self, methods=['GET'])
    if self.__module__.get("actions", {}):
      app.add_url_rule('/%s/<action>'%self.__name__, view_func = self, methods=['GET', 'POST'])
      app.add_url_rule('/%s/<action>/<_id>'%self.__name__, view_func = self, methods=['GET', 'POST'])

  @check_module_access
  def __call__(self, action = None, _id = None):
    if _id is None and action is None: return self.__module__["base"]["function"](self.__module__)
    form = self.__module__["actions"][action]["function"]
    if request.method == 'GET': return form(self.__module__, action, _id)
    if request.method == 'POST': return form(self.__module__, action, _id, request.form)

  def __repr__(self):
    return "<TableView: %s>"%self.__name__


for module in [
                employee_module,
                card_module,
                finance_module,
                finance_report_module,
                children_module,
                children_report_module,
                place_module,
                role_module,
                user_module,
                app_module,
              ]:
  registrate_view(module)
  TableView(app, module)
