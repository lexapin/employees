-- Схема

-- Вариант 10.
-- Л. р. №1. Создание и заполнение отношений БД библиотеки.
-- 1. Отношение "Журналы" (поля "Индекс журнала", "Название" и "Издатель").
-- 2. Отношение "Рубрикатор" (поля "Шифр" и "Название рубрики").
-- 3. Отношение "Выпуски журналов" (поля "Идентификатор", "Индекс журнала", "Год", "Номер выпуска").
-- 4. Отношение "Публикации":
-- Содержимое поля Тип Длина Дес. Примечание
-- Автор(ы) публикации С 50 ключевая комбинация полей
-- Название публикации C 60 
-- Идентификатор выпуска N 6 0

-- Шифр рубрики C 6 внешний ключ к таблице "Рубрикатор"
-- Страницы С 7 например, с.56-62
-- Примечание C 30 название раздела журнала
-- Примечание: не для всех отношений указаны ключевые поля. Если они не указаны, их нужно добавить!

CREATE SEQUENCE journal_seq
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;

CREATE TABLE journal (
  id numeric(10) not null,
  zip varchar2(50) not null,
  title varchar2(50) not null,
  publisher varchar2(50),
  CONSTRAINT id_journal PRIMARY KEY (id)
);

CREATE SEQUENCE category_seq
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;

CREATE TABLE category(
  id numeric(10) not null,
  name varchar2(50) not null,
  code varchar2(50) not null,
  journal_id numeric(10) not null,
  CONSTRAINT id_category PRIMARY KEY (id),
  CONSTRAINT fk_category_journal
    FOREIGN KEY (journal_id)
    REFERENCES journal(id)
);

CREATE SEQUENCE release_seq
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;

CREATE TABLE release(
  id numeric(10) not null,
  release_index varchar2(50) not null,
  release_year numeric(10) not null,
  release_number numeric(10) not null,
  journal_id numeric(10) not null,
  CONSTRAINT id_release PRIMARY KEY (id),
  CONSTRAINT fk_release_journal
    FOREIGN KEY (journal_id)
    REFERENCES journal(id)
);

CREATE SEQUENCE author_seq
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;

CREATE TABLE author(
  id numeric(10) not null,
  name varchar2(50) not null,
  year_of_birth numeric(10) not null,
  CONSTRAINT id_author PRIMARY KEY (id)
);

CREATE SEQUENCE article_seq
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;

CREATE TABLE article(
  id numeric(10) not null,
  title varchar2(50) not null,
  pages varchar2(50) not null,
  note varchar2(50) not null,
  release_id numeric(10) not null,
  category_id numeric(10) not null,
  CONSTRAINT id_article PRIMARY KEY (id),
  CONSTRAINT fk_release_article
    FOREIGN KEY (release_id)
    REFERENCES release(id),
  CONSTRAINT fk_category_article
    FOREIGN KEY (category_id)
    REFERENCES category(id)
);

CREATE SEQUENCE article_author_seq
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;

CREATE TABLE article_author(
  id numeric(10) not null,
  author_id numeric(10) not null,
  article_id numeric(10) not null,
  CONSTRAINT id_article_author PRIMARY KEY (id),
  CONSTRAINT fk_article_author
    FOREIGN KEY (author_id)
    REFERENCES author(id),
  CONSTRAINT fk_author_article
    FOREIGN KEY (article_id)
    REFERENCES article(id)
);

-- Заполнение данных
INSERT INTO journal (id, zip, title, publisher)
VALUES (journal_seq.nextval, '428000', 'Базы данных', 'ДМК ПРЕСС');

INSERT INTO category (id, name, code, journal_id)
    SELECT
       category_seq.nextval AS id,
       'СУБД' AS name,
       '1234' AS code,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );

INSERT INTO category (id, name, code, journal_id)
    SELECT
       category_seq.nextval AS id,
       'Технологии' AS name,
       '5678' AS code,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );

INSERT INTO category (id, name, code, journal_id)
    SELECT
       category_seq.nextval AS id,
       'Базы данных' AS name,
       '9012' AS code,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );

INSERT INTO release (id, release_index, release_year, release_number, journal_id)
    SELECT
       release_seq.nextval AS id,
       'fdh.23' AS release_index,
       2017 AS release_year,
       10 AS release_number,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );

INSERT INTO release (id, release_index, release_year, release_number, journal_id)
    SELECT
       release_seq.nextval AS id,
       'fdh.23' AS release_index,
       2015 AS release_year,
       4 AS release_number,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );


INSERT INTO release (id, release_index, release_year, release_number, journal_id)
    SELECT
       release_seq.nextval AS id,
       'fdh.23' AS release_index,
       1999 AS release_year,
       7 AS release_number,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );


INSERT INTO journal (id, zip, title, publisher)
VALUES (journal_seq.nextval, '428027', 'Хакер', 'Волга печать');

INSERT INTO category (id, name, code, journal_id)
    SELECT
       category_seq.nextval AS id,
       'СУБД' AS name,
       '1234' AS code,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );

INSERT INTO category (id, name, code, journal_id)
    SELECT
       category_seq.nextval AS id,
       'Технологии' AS name,
       '5678' AS code,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );

INSERT INTO category (id, name, code, journal_id)
    SELECT
       category_seq.nextval AS id,
       'История' AS name,
       '9012' AS code,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );

INSERT INTO release (id, release_index, release_year, release_number, journal_id)
    SELECT
       release_seq.nextval AS id,
       'fdh.23' AS release_index,
       2005 AS release_year,
       12 AS release_number,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );

INSERT INTO release (id, release_index, release_year, release_number, journal_id)
    SELECT
       release_seq.nextval AS id,
       'fdh.23' AS release_index,
       2010 AS release_year,
       2 AS release_number,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );


INSERT INTO release (id, release_index, release_year, release_number, journal_id)
    SELECT
       release_seq.nextval AS id,
       'fdh.23' AS release_index,
       1995 AS release_year,
       8 AS release_number,
       journal.id AS journal_id
    FROM journal
    WHERE journal.id = ( SELECT MAX(id) FROM journal );


INSERT INTO author (id, name, year_of_birth) VALUES (author_seq.nextval, 'Фомин Алексей', 1986);
INSERT INTO author (id, name, year_of_birth) VALUES (author_seq.nextval, 'Антонов Владислав', 1954);
INSERT INTO author (id, name, year_of_birth) VALUES (author_seq.nextval, 'Майоров Алексей', 1988);

SELECT title, release_number, name
FROM journal, release, category
WHERE release.journal_id=journal.id
AND journal.id=category.journal_id;


INSERT INTO article (id, title, pages, note, release_id, category_id)
    SELECT
       article_seq.nextval AS id,
       'Статья 1' AS title,
       'с.1-5' AS pages,
       'О статье 1' AS note,
       release.id AS release_id,
       category.id AS category_id
    FROM journal, release, category
    WHERE release.journal_id=journal.id
    AND journal.id=category.journal_id
    AND category.name='СУБД';

INSERT INTO article_author (id, author_id, article_id)
    SELECT
      article_author_seq.nextval AS id,
      author.id AS author_id,
      article.id AS article_id
    FROM article, author
    WHERE article.title='Статья 1'
    AND author.name='Фомин Алексей';


INSERT INTO article (id, title, pages, note, release_id, category_id)
    SELECT
       article_seq.nextval AS id,
       'Статья 2' AS title,
       'с.10-15' AS pages,
       'О статье 2' AS note,
       release.id AS release_id,
       category.id AS category_id
    FROM journal, release, category
    WHERE release.journal_id=journal.id
    AND journal.id=category.journal_id
    AND category.name='Базы данных';

INSERT INTO article_author (id, author_id, article_id)
    SELECT
      article_author_seq.nextval AS id,
      author.id AS author_id,
      article.id AS article_id
    FROM article, author
    WHERE article.title='Статья 2'
    AND author.name='Антонов Владислав';


INSERT INTO article (id, title, pages, note, release_id, category_id)
    SELECT
       article_seq.nextval AS id,
       'Статья 3' AS title,
       'с.20-25' AS pages,
       'О статье 3' AS note,
       release.id AS release_id,
       category.id AS category_id
    FROM journal, release, category
    WHERE release.journal_id=journal.id
    AND journal.id=category.journal_id
    AND category.name='Технологии';

INSERT INTO article_author (id, author_id, article_id)
    SELECT
      article_author_seq.nextval AS id,
      author.id AS author_id,
      article.id AS article_id
    FROM article, author
    WHERE article.title='Статья 3'
    AND author.name='Майоров Алексей';

-- Выборка данных
ЛАБА2

SELECT journal.title, article.title, category.name, author.name, release.release_year
FROM article, release, category, journal, article_author, author
WHERE article.release_id=release.id
AND article.category_id=category.id
AND article_author.author_id=author.id
AND article_author.article_id=article.id
AND release.release_year>EXTRACT(YEAR FROM sysdate)-3
ORDER BY journal.title, article.title, category.name, author.name, release.release_year;


SELECT journal.title, article.title, category.name, author.name, release.release_year
FROM article, release, category, journal, article_author, author
WHERE article.release_id=release.id
AND article.category_id=category.id
AND article_author.author_id=author.id
AND article_author.article_id=article.id
AND (category.name='СУБД' OR category.name='Базы данных')
ORDER BY journal.title, article.title, category.name, author.name, release.release_year;


select category.name
from category
where category.name not in (select category.name from category, article where article.category_id=category.id group by category.name)
group by category.name;


SELECT journal.title, article.title, category.name, author.name, release.release_year
FROM article, release, category, journal, article_author, author
WHERE article.release_id=release.id
AND article.category_id=category.id
AND article_author.author_id=author.id
AND article_author.article_id=article.id
AND author.name='Майоров Алексей'
ORDER BY journal.title, article.title, category.name, author.name, release.release_year;

-- Представления данных
CREATE VIEW articles as
  SELECT 
    journal.title AS journal_name,
    article.title AS article_name,
    category.name as category_name,
    author.name as author_name,
    release.release_year
  FROM article, release, category, journal, article_author, author
  WHERE article.release_id=release.id
  AND article.category_id=category.id
  AND article_author.author_id=author.id
  AND article_author.article_id=article.id
  ORDER BY journal.title, article.title, category.name, author.name, release.release_year;

select * from articles;

create view journal_statistics as
  select journal_title1 as title, category_name1 as name, journal_count1 as before_2000, journal_count2 as after_2000
  from (
    select journal.title as journal_title1, category.name as category_name1, count(*) as journal_count1
    from release, article, journal, category
    where release.id=article.release_id
    and release.journal_id=journal.id
    and article.category_id=category.id
    and release.release_year<2000
    group by journal.title, category.name), (
    select journal.title as journal_title2, category.name as category_name2,  count(*) as journal_count2
    from release, article, journal, category
    where release.id=article.release_id
    and release.journal_id=journal.id
    and article.category_id=category.id
    and release.release_year>2000
    group by journal.title, category.name)
  where journal_title1=journal_title2 and category_name1=category_name2;

create view journal_statistics as
  select journal.title, release.release_year, count(*)
  from release, article, journal
  where release.id=article.release_id
  and release.journal_id=journal.id
  group by journal.title, release.release_year
  order by journal.title, release.release_year;