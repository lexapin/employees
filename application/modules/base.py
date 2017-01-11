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


def update_function(module, action, _id = None, data = None):
  GET_QUERY = module["actions"][action]["get_query"]
  SET_QUERY = module["actions"][action]["set_query"]
  if data is None:
    db_items = None if _id is None else get_data_from_db(GET_QUERY%(_id,))[0]
    disabled = ["_id"] if _id is None else []
    return render_template("form.html", 
                            items = create_form_items(module, view = None, values = db_items, disabled = disabled),
                            base = module["base"],
                            decode = create_decode_table(module),
                          )
  else:
    if _id is not None:
      if not get_data_from_db(GET_QUERY%(_id,)) or _id != data["_id"]:
        flash(u"Данные введены некорректно!!!")
        return redirect(url_for('index'))
    attrs = []
    try:
      for attr in module["actions"][action]["attrs"]: attrs.append(data[attr])
      set_data_to_db(SET_QUERY%attrs)
    except Exception as err:
      flash(u"Ошибка в процессе записи в базу данных новых значений")
      flash(str(err))
      flash(u"%s"%SET_QUERY)
      flash(u"%s"%str(attrs))
    else:
      flash(u"Данные успешно изменены")
    return redirect(url_for('index'))

def delete_function(module, _id):
  return redirect(url_for('index'))