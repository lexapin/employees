# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask.ext.login import LoginManager, AnonymousUser, current_user
from app.user import User
from functools import wraps

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = u"Зарегестрируйтесь или войдите!"
login_manager.login_message_category = "info"


class Anonymous(AnonymousUser):
  def __init__(self):
    self.username = "guest"

  def __repr__(self):
    return u"Гость"

  def is_anonymous(self):
    return True

login_manager.anonymous_user = Anonymous

@login_manager.user_loader
def load_user(_id):
  return User.get(int(_id)) if (_id is not None) else None


def login_required_when_anonymous(func):
  @wraps(func)
  def decorated_view(*args, **kwargs):
    if (current_user.is_anonymous()):
      return login_manager.unauthorized()
    return func(*args, **kwargs)
  return decorated_view