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


finance_module = {
  "base": {
    "name": "employees",
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