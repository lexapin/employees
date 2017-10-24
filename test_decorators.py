# -*- coding: utf-8 -*-
import copy

print "init"

def is_auth(func):
  print "-----INIT-FUNCTION-----"
  def wrap_func(*args, **kwargs):
    print "-----RUN-FUNCTION-----"
    return func(*args, **kwargs)
  return wrap_func

class Function(object):
  """docstring for Function"""
  def __init__(self, caption, default, name):
    super(Function, self).__init__()
    self.caption = caption
    self.default = default
    self.name = name
    
  @is_auth
  def __call__(self, user = None):
    if user is None: user = self.default
    print self.caption%user

  def __repr__(self):
    return "<Function: %s>"%self.name

print "MAIN PROGRAMM"
data = [
          {"name":"russian_hello", "caption": "ПРИВЕТ, %s", "default": "Русский Ваня"},
          {"name":"english_hello", "caption": "HELLO, %s", "default": "Anonymous"},
        ]
functions = {}
for obj in data:
  name = obj["name"]
  caption = obj["caption"]
  default = obj["default"]
  function = Function(caption, default, name)
  functions[name] = function


print "init complete"
print functions
for function in functions.values():
  function()

for function in functions.values():
  function("Fomin")