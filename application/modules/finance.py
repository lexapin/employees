# -*- coding: utf-8 -*-
from base import *


six_month_query = """
SELECT employee_id, first_name, last_name, sum_salary, sum_bonus, (sum_salary+sum_bonus) AS itog, ((sum_salary+sum_bonus)*0.13) AS tax
FROM (SELECT employee_id, first_name, last_name, SUM(salary) AS sum_salary, SUM(bonus) AS sum_bonus
FROM employee
INNER JOIN employee_month_pay_association
INNER JOIN month_pay
INNER JOIN (SELECT month, year FROM month_pay GROUP BY (year*100+month) ORDER BY (year*100+month) DESC LIMIT 6) d_m
WHERE month_pay.id=month_pay_id AND month_pay.month=d_m.month AND month_pay.year=d_m.year AND employee_id = employee.id
GROUP BY employee_id) as report;
"""

salary_query = """
SELECT month_pay_id, CONCAT(first_name, " ", last_name), month, year, salary, bonus
FROM employee
INNER JOIN employee_month_pay_association
INNER JOIN month_pay 
WHERE employee.id=employee_id AND month_pay.id=month_pay_id
ORDER BY (year*100+month) DESC;
"""

add_finance_information_query = """
INSERT INTO month_pay (month, year, salary, bonus)
SELECT * FROM (SELECT %s AS month, %s AS year, %s AS salary, %s AS bonus) AS tmp
WHERE NOT EXISTS (
SELECT employee_id, month, year
FROM employee_month_pay_association
INNER JOIN month_pay
WHERE month_pay.id=month_pay_id AND month=%s AND year=%s AND employee_id=%s
) LIMIT 1;
"""

get_form_to_update_finance_info_query = """
SELECT month_pay.id, employee_id, month, year, salary, bonus
FROM employee_month_pay_association
INNER JOIN month_pay 
WHERE month_pay_id = %s AND month_pay.id=month_pay_id;
"""


finance_report_module = {
  "base": {
    "name": "halfyearreport",
    "title": u"Отчетность по зарплате за 6 месяцев",
    "table_caption": u"Отчетность по зарплате за 6 месяцев",
    "form_caption": u"Имя, Фамилия, полугодовая зарплата сотрудника сотрудника",
    "function": table_view,
    "query": six_month_query,
  },
  "contextmenu_actions": [],
  "buttonsmenu_actions": [],
  "actions": {},
  "attributes": {
    "_id": {
      "position": 0,
      "caption": u"#",
      "type": int,
    },
    "first_name": {
      "position": 1,
      "caption": u"Имя",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "last_name": {
      "position": 2,
      "caption": u"Фамилия",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": basestring,
    },
    "salary": {
      "position": 3,
      "caption": u"Оклад",
      "decode_function": lambda value: str(value),
      "type": basestring,
    },
    "bonus": {
      "position": 4,
      "caption": u"Премия",
      "decode_function": lambda value: str(value),
      "type": basestring,
    },
    "sum": {
      "position": 5,
      "caption": u"Всего выплат",
      "decode_function": lambda value: str(value),
      "type": basestring,
    },
    "tax": {
      "position": 6,
      "caption": u"НДФЛ",
      "decode_function": lambda value: str(value),
      "type": basestring,
    },
  },
}


def add_employee_month_pay_association(data):
  data = tuple(data)
  set_data_to_db("INSERT INTO employee_month_pay_association (month_pay_id, employee_id) values (%s, %s);"%(data))
  return


finance_module = {
  "base": {
    "name": "finance",
    "title": u"Бухгалтерская ведомость по зарплате",
    "table_caption": u"Бухгалтерская ведомость по зарплате",
    "form_caption": u"Информация о зарплате сотрудника",
    "function": table_view,
    "query": salary_query,
  },
  "contextmenu_actions": ["edit"],
  "buttonsmenu_actions": ["add"],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": add_finance_information_query,
      "attrs": ["month", "year", "salary", "bonus", "month", "year", "name"],
      "trigger": add_employee_month_pay_association,
      "vars_to_trigger": ["name"],
      "disabled": ["_id"],
    },
    "edit": {
      "caption": u"Редактировать",
      "function": update_function,
      "get_query": get_form_to_update_finance_info_query,
      "set_query": "UPDATE month_pay SET salary='%s', bonus='%s' WHERE id = %s;",
      "attrs": ["salary", "bonus", "_id"],
    },
  },
  "attributes": {
    "_id": {
      "position": 0,
      "caption": u"#",
      "type": int,
    },
    "name": {
      "position": 1,
      "caption": u"Имя, Фамилия",
      "decode_function": lambda value: value.decode("utf-8"),
      "type": list,
      "values_query": "SELECT id, CONCAT(first_name, ' ', last_name) FROM employee;",
    },
    "month": {
      "position": 2,
      "caption": u"Месяц",
      "decode_function": lambda value: str(value),
      "type": basestring,
    },
    "year": {
      "position": 3,
      "caption": u"Год",
      "decode_function": lambda value: str(value),
      "type": basestring,
    },
    "salary": {
      "position": 4,
      "caption": u"Оклад",
      "decode_function": lambda value: str(value),
      "type": basestring,
    },
    "bonus": {
      "position": 5,
      "caption": u"Премия",
      "decode_function": lambda value: str(value),
      "type": basestring,
    },
  },
}