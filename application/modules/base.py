# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash
from utilites import *
def table_view(module):
  data = get_data_from_db(module["base"]["query"])
  return render_template("table.html",
                  base = module["base"],
                  contextmenu = create_context_menu(module),
                  buttonsmenu = create_buttons_menu(module),
                  header = create_table_header(module),
                  decode = create_decode_table(module),
                  data = data,
                  )


def update_function(module, _id = None, data = None):
  GET_QUERY = "SELECT id, first_name, last_name FROM employee WHERE id=%s;"
  UPDATE_QUERY = """
  UPDATE employee SET first_name="%s", last_name="%s"
  WHERE id = %s;
  """
  INSERT_QUERY = "INSERT INTO employee (first_name, last_name) VALUES ('%s', '%s');"
  if data is None:
    db_items = None if _id is None else get_data_from_db(GET_QUERY%(_id,))[0]
    disabled = ["_id"] if _id is None else []
    return render_template("form.html", 
                            items = create_form_items(module, view = None, values = db_items, disabled = disabled),
                            base = module["base"],
                            decode = create_decode_table(module),
                          )
  else:
    if (_id is not None) and ( (not get_data_from_db(GET_QUERY%(_id,)) ) or ( _id != data["_id"]) ):
      flash(u"Данные о сотруднике введены некорректно!!!")
      return redirect(url_for('index'))
    first_name = data["first_name"]
    last_name = data["last_name"]
    try:
      if _id is None: set_data_to_db(INSERT_QUERY%(first_name, last_name))
      else: set_data_to_db(UPDATE_QUERY%(first_name, last_name, _id))
    except Exception as err:
      flash(u"Ошибка в процессе записи в базу данных новых значений")
      flash(str(err))
    else:
      flash(u"Данные успешно изменены")
    return redirect(url_for('index'))

def delete_function(module, _id):
  return redirect(url_for('index'))