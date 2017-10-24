# employees (robot4.pythonanywhere.com)
БД сотрудников предприятия

Распределить права доступамежду между ролями
  1. Админ
  2. Руководитель
  3. Профсоюзный лидер
  4. Кадровик
  5. Бухгалтер

Информация о сотруднике:
  1. Личный листок учета кадров
  2. Финансовая информация
  
Отчеты:
  1. з.п. за пол-года (основная часть + стимулирующая +д премия) - НДФЛ.
  2. дети до 15 лет на 1 января следующего года.

Отображаемая информация для каждой роли должна отличаться:
  1. Админ - все кроме финансов
  2. Руководитель - все
  3. Профсоюзный лидер - ФИО, ДР, Место жительства, дети
  4. Кадровик - кадровый листок без финансов
  5. Бухгалтер - ФИО, ДР, отдел, должность, сведения о детях, финансы


application data diagramm (схема данных приложения)

              user 
               /∞
              /
             /1
           role
          1/  \∞
          /    \
        ∞/      \∞
    action      view
        ∞\______/1

    roles:
      administrator (Администратор)
      boss (Руководитель)
      booker (Бухгалтер)
      personnel officer (Кадровый сотрудник)
      trade union leader (Профсоюзный лидер)

    views:
      base:
        employee-children (дети сотрудника)
        employee-address (место жительства сотрудника)
        employee-cards (личные листки учета кадров)
        employee-finance (зарплата)
      query:
        employee-children(up 1 to 13 years old)
        employee-pay(by three months)

    actions:
      add-employee-card (добавить карточку сотрудника)
      rem-employee-card (удалить карточку сотрудника)
      mod-employee-card (изменить карточку сотрудника)
      change-position (изменить должность сотрудника)
      change-address (изменить адрес сотрудника)
      add-child (добавить ребенка сотрудника)
      set-month-pay (добавить свдения о з/п за текущий месяц)


information model ontology (онтология информационной модели)

                  1 1
         employee --- card
          |1         /1  \1
          |         /     \
          |∞        |∞    |∞
    month_pay     place  child

    employee (сотрудник)
      first_name
      last_name
      owner_card
      pays

    month_pay (начисленная зарплата)
      month
      year
      salary
      bonus

    card (личная карточка учета кадров)
      info
      birth_day
      children
      positions

    place (должность)
      place_name
      assign_date

    child (ребенок)
      first_name
      birth_day
