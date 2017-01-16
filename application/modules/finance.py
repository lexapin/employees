# -*- coding: utf-8 -*-
from base import *


six_month_query = """
SELECT employee_id, first_name, last_name, SUM(salary), SUM(bonus)
FROM employee
INNER JOIN employee_month_pay_association
INNER JOIN month_pay
INNER JOIN (SELECT month, year FROM month_pay GROUP BY (year*100+month) ORDER BY (year*100+month) DESC LIMIT 2) d_m
WHERE month_pay.id=month_pay_id AND month_pay.month=d_m.month AND month_pay.year=d_m.year AND employee_id = employee.id
GROUP BY employee_id;
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
  },
}


def add_employee_month_pay_association(data):
  data = tuple(data)
  set_data_to_db("INSERT INTO employee_month_pay_association (month_pay_id, employee_id) values (%s, %s);"%(data))
  return


finance_module = {
  "base": {
    "name": "finance",
    "title": u"Бухгалтерская отчетность по зарплате",
    "table_caption": u"Бухгалтерская отчетность по зарплате",
    "form_caption": u"Информация о зарплате сотрудника",
    "function": table_view,
    "query": """
SELECT employee.id, CONCAT(first_name, " ", last_name), month, year, salary, bonus
FROM employee
INNER JOIN employee_month_pay_association
INNER JOIN month_pay 
WHERE employee.id=employee_id AND month_pay.id=month_pay_id
ORDER BY (year*100+month) DESC;
""",
  },
  "contextmenu_actions": ["edit"],
  "buttonsmenu_actions": ["add"],
  "actions": {
    "add": {
      "caption": u"Добавить",
      "function": update_function,
      "set_query": """
INSERT INTO month_pay (month, year, salary, bonus)
SELECT * FROM (SELECT %s AS month, %s AS year, %s AS salary, %s AS bonus) AS tmp
WHERE NOT EXISTS (
SELECT employee_id, month, year
FROM employee_month_pay_association
INNER JOIN month_pay
WHERE month_pay.id=month_pay_id AND month=%s AND year=%s AND employee_id=%s
) LIMIT 1;
      """,
      "attrs": ["month", "year", "salary", "bonus", "month", "year", "name"],
      "trigger": add_employee_month_pay_association,
      "vars_to_trigger": ["name"],
      "disabled": ["_id"],
    },
    "edit": {
      "caption": u"Обновить",
      "function": update_function,
      "get_query": """
SELECT month_pay.id, employee_id, month, year, salary, bonus
FROM employee_month_pay_association
INNER JOIN month_pay 
WHERE employee_id = %s AND month_pay.id=month_pay_id;
      """,
      "set_query": "UPDATE employee SET first_name='%s', last_name='%s' WHERE id = %s;",
      "attrs": ["month", "year", "salary", "bonus", "month", "year", "name"],
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
      "values_query": "SELECT id, first_name, last_name FROM employee;",
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

"""
INSERT INTO month_pay (month, year, salary, bonus) VALUES (1, 2017, 10000, 5000);
INSERT INTO employee_month_pay_association (employee_id, month_pay_id) VALUES (1, 1);
INSERT INTO month_pay (month, year, salary, bonus) VALUES (2, 2017, 10000, 5000);
INSERT INTO employee_month_pay_association (employee_id, month_pay_id) VALUES (1, 2);
INSERT INTO month_pay (month, year, salary, bonus) VALUES (3, 2017, 10000, 5000);
INSERT INTO employee_month_pay_association (employee_id, month_pay_id) VALUES (1, 3);
INSERT INTO month_pay (month, year, salary, bonus) VALUES (1, 2017, 15000, 5000);
INSERT INTO employee_month_pay_association (employee_id, month_pay_id) VALUES (2, 4);
INSERT INTO month_pay (month, year, salary, bonus) VALUES (2, 2017, 15000, 5000);
INSERT INTO employee_month_pay_association (employee_id, month_pay_id) VALUES (2, 5);
INSERT INTO month_pay (month, year, salary, bonus) VALUES (3, 2017, 15000, 5000);
INSERT INTO employee_month_pay_association (employee_id, month_pay_id) VALUES (2, 6);
INSERT INTO month_pay (month, year, salary, bonus) VALUES (4, 2017, 15000, 4000);
INSERT INTO employee_month_pay_association (employee_id, month_pay_id) VALUES (2, 4);
INSERT INTO month_pay (month, year, salary, bonus) VALUES (4, 2017, 12000, 6000);
INSERT INTO employee_month_pay_association (employee_id, month_pay_id) VALUES (1, 10);
"""

"""
SELECT employee.id, first_name, last_name, month, year, salary, bonus
FROM employee
INNER JOIN employee_month_pay_association
INNER JOIN month_pay 
WHERE employee.id=employee_id AND month_pay.id=month_pay_id;
"""

"""
SELECT employee.id, first_name, last_name, month, year, salary, bonus
FROM employee
INNER JOIN employee_month_pay_association
INNER JOIN month_pay 
WHERE employee.id=employee_id AND month_pay.id=month_pay_id
AND month_pay_id IN (SELECT MAX(month_pay_id) FROM employee_month_pay_association GROUP BY employee_id);
"""

"""
SELECT employee_id, first_name, last_name, SUM(salary), SUM(bonus)
FROM employee
INNER JOIN employee_month_pay_association
INNER JOIN month_pay
INNER JOIN (SELECT month, year FROM month_pay GROUP BY (year*100+month) ORDER BY (year*100+month) DESC LIMIT 2) d_m
WHERE month_pay.id=month_pay_id AND month_pay.month=d_m.month AND month_pay.year=d_m.year AND employee_id = employee.id
GROUP BY employee_id;
"""

"""
SELECT month, year FROM month_pay
GROUP BY (year*100+month)
ORDER BY (year*100+month) DESC
LIMIT 2;
"""


"""
INSERT INTO month_pay (month, year, salary, bonus)
SELECT * FROM (SELECT %(month)s, %(year)s, %(salary)s, %(bonus)s) AS tmp
WHERE NOT EXISTS (
SELECT employee_id, month, year
FROM employee_month_pay_association
INNER JOIN month_pay
WHERE month_pay.id=month_pay_id AND month=%(month)s AND year=%(year)s
) LIMIT 1;
"""

"""
INSERT INTO month_pay (month, year, salary, bonus)
SELECT * FROM (SELECT 12 as month, 2016 as year, 5000 as salary, 5000 as bonus) AS tmp
WHERE NOT EXISTS (
SELECT employee_id, month, year
FROM employee_month_pay_association
INNER JOIN month_pay
WHERE month_pay.id=month_pay_id AND month=12 AND year=2016 AND employee_id=1
) LIMIT 1;
"""



"""
SELECT * 
FROM month_pay
ORDER BY (year*100+month) DESC
LIMIT (SELECT COUNT(*) FROM employee WHERE id IN (SELECT employee_id FROM employee_month_pay_association GROUP BY employee_id));
"""

"""
SELECT month_pay_id, employee_id, month, year
FROM employee_month_pay_association
INNER JOIN month_pay
WHERE month_pay.id=month_pay_id
GROUP BY (year*100+month)
"""

"""
SELECT MAX(month_pay_id)
FROM employee_month_pay_association
GROUP BY employee_id;
"""