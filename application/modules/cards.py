# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash
from utilites import *

employee_module = {
  "module": {
    "name": "employees",
    "caption": u"Сотрудники предприятия (базовая таблица)",
  },
  "contextmenu_actions": ["edit", "delete",],
  "button_actions": ["add",],
  "actions": {
    "add": {
      "caption": u"Добавить",
    },
    "edit": {
      "caption": u"Редактировать",
    },
    "delete": {
      "caption": u"Удалить",
    },
  },
  "attributes": {
    "_id": {
      "caption": u"#",
      "type": int,
    },
    "first_name": {
      "caption": u"Имя",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "last_name": {
      "caption": u"Фамилия",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
  },
}

employee_contextmenu = {
  "module": {
    "name": "employees",
    "caption": u"Сотрудники предприятия (базовая таблица)",
  },
  "actions": [
    {
      "name": "edit",
      "caption": u"Редактировать",
    },
    {
      "name": "delete",
      "caption": u"Удалить",
    },
  ]
}

employee_decodes = {
  0: lambda value: value,
  1: lambda value: value.decode("utf-8"),
  2: lambda value: value.decode("utf-8"),
}

def employees():
  QUERY = "SELECT id, first_name, last_name FROM employee;"
  data = get_data_from_db(QUERY)
  employee_actions = [
    dict(
      name = "add",
      caption = "Добавить",
    ),
  ]
  return render_template("table.html",
                  title = u"Сотрудники предприятия (базовая таблица)",
                  data = data, 
                  header = [u"#", u"Имя", u"Фамилия"],
                  contextmenu = employee_contextmenu,
                  decode = employee_decodes,
                  actions = employee_actions,
                  )


def employee_form(_id, data = None):
  GET_QUERY = "SELECT id, first_name, last_name FROM employee WHERE id=%s;"%(_id,)
  UPDATE_QUERY = """
  UPDATE employee SET first_name="%s", last_name="%s"
  WHERE id = %s;
  """
  if data is None:
    employee = get_data_from_db(GET_QUERY)
    if employee:
      employee = employee[0]
      employee = [
        dict(
          type = "text",
          id = "_id",
          name = "_id",
          placeholder = u"#",
          value = employee[0],
          readonly = True,
          ),
        dict(
          type = "text",
          id = "first_name",
          name = "first_name",
          placeholder = u"Имя",
          value = employee[1],
          readonly = False,
          ),
        dict(
          type = "text",
          id = "last_name",
          name = "last_name",
          placeholder = u"Фамилия",
          value = employee[2],
          readonly = False,
          ),
      ]
      return render_template("form.html", 
                              items = employee,
                              title = u"Основная информация о сотруднике",
                              decode = employee_decodes,
                            )
    else:
      flash(u"Информация о сотруднике не найдена")
      return redirect(url_for('index'))
  else:
    if not get_data_from_db(GET_QUERY) or _id != data["_id"]:
      flash(u"Данные о сотруднике введены некорректно!!!")
      return redirect(url_for('index'))
    first_name = data["first_name"]
    last_name = data["last_name"]
    try:
      data = set_data_to_db(UPDATE_QUERY%(first_name, last_name, _id))
    except Exception as err:
      flash(u"Ошибка в процессе изменения данных")
      flash(str(err))
    else:
      flash(u"Данные успешно изменены")
    return redirect(url_for('index'))


def add_employee(data = None):
  INSERT_QUERY = "INSERT INTO "
  if data is None:
    return render_template("form.html", 
                              items = employee,
                              title = u"Основная информация о сотруднике",
                              decode = employee_decodes,
                            )
  else:
    first_name = data["first_name"]
    last_name = data["last_name"]
    try:
      data = set_data_to_db(UPDATE_QUERY%(first_name, last_name, _id))
    except Exception as err:
      flash(u"Ошибка в процессе изменения данных")
      flash(str(err))
    else:
      flash(u"Данные успешно изменены")
    return redirect(url_for('index'))

"""
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `first_name` varchar(20),
  `last_name` varchar(20)
);

CREATE TABLE `card` (
  `id` int NOT NULL AUTO_INCREMENT primary key,
  `employee_id` int NOT NULL,
  `personnel_number` varchar(20),
  `nature of work`   varchar(20),
  `type_of_work`     varchar(20),
  `date_of_birth`    int(11),
  `place_of_birth`   varchar(20),
  `education`        varchar(20),
  `foreign_language` varchar(20),
  FOREIGN KEY (employee_id)
        REFERENCES employee(id)
);

insert into employee (first_name, last_name) values ("Алексей", "Фомин");
insert into card (
  employee_id,
  personnel_number,
  nature_of_work,
  type_of_work,
  date_of_birth,
  place_of_birth,
  education,
  foreign_language
) values(
  1,
  "1320",
  "офис",
  "инженер",
  508118400,
  "Чебоксары",
  "ЧГУ им.И.Н.Ульянова(2010)",
  "английский"
);
insert into employee (first_name, last_name) values ("Михаил", "Инюшкин");
insert into card (
  employee_id,
  personnel_number,
  nature_of_work,
  type_of_work,
  date_of_birth,
  place_of_birth,
  education,
  foreign_language
) values(
  2,
  "1800",
  "офис",
  "инженер-программист",
  609984000,
  "Чебоксары",
  "ЧГУ им.И.Н.Ульянова(2012)",
  "английский"
);

"""