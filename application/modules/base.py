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


def update_function(module, action, _id = None, request_data = None):
  GET_QUERY = module["actions"][action].get("get_query", None)
  SET_QUERY = module["actions"][action].get("set_query", None)
  if request_data is None:
    db_items = None if _id is None else get_data_from_db(GET_QUERY%(_id,))[0]
    disabled = module["actions"][action].get("disabled", [])
    return render_template("form.html", 
                            items = create_form_items(module, view = None, values = db_items, disabled = disabled),
                            base = module["base"],
                            decode = create_decode_table(module),
                          )
  else:
    # Мешает менять данные, надо что-то новое придумать для защиты вводимой информации
    # if _id is not None:
    #   if not get_data_from_db(GET_QUERY%(_id,)) or _id != request_data["_id"]:
    #     flash(u"Данные введены некорректно!!!")
    #     return redirect(url_for(module["base"]["name"]))
    try:
      encode_function = lambda attr: module["attributes"][attr].get("encode_function", lambda value: value)
      response_data = set_data_to_db(SET_QUERY%tuple(encode_function(attr)(request_data[attr]) for attr in module["actions"][action]["attrs"]))
    except Exception as err:
      flash(u"Ошибка в процессе записи в базу данных новых значений")
      flash(str(err))
      flash(u"%s"%SET_QUERY)
      flash(u"%s"%str(tuple(request_data[attr] for attr in module["actions"][action]["attrs"])))
    else:
      flash(u"Данные успешно изменены")
      flash(u"%s"%response_data)
      trigger_function = module["actions"][action].get("trigger", lambda value: None)
      trigger_attrs = module["actions"][action].get("vars_to_trigger", [])
      response_data = [response_data]
      for attr in trigger_attrs:
        encode_function = lambda attr: module["attributes"][attr].get("encode_function", lambda value: value)
        response_data.append(encode_function(attr)(request_data[attr]))
      trigger_function(response_data)
    return redirect(url_for(module["base"]["name"]))

def delete_function(module, _id):
  return redirect(url_for(module["base"]["name"]))