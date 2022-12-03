# gladwellproject
Project for timetracking and goal setting in work environment

## Техническое задание
Сервис должен уметь:
- Хранить данные о потраченном времени и поставленных целях (Postgre + DjangoAdmin)
- Добавлять новые категории/активности для потраченного времени (FastAPI)

- Учитывать связь потраченного времени и целей, на которые мы тратит время (Analytics)
- Уведомлять пользователей о необходимых действиях и достигнутых целях (Notifications)
- Давать возможность полнотекстового поиска (Elastic Search)

## Development
Если вы хотите развивать данный проект и вносить изменения, то вам понадобятся:
### Pre-commit Hooks
Это удобные хуки перед коммитом, которые проверят ваш код на соответствие стилевым стандартам. Устанавливаем их этой командой:
```$ pre-commit install```


## Структура Postgre БД gladwell

table users:
		"Хранит Юзеров"
		user_id uuid
		email email_field
		name varchar(250)
		goals_achieved integer
		register_date Date


table users_goals:
		user_id
		goal_id

table goals:
		"Хранит цели"
		goal_id uuid
		name varchar(250)
		description text
		created_at date
		updated_at date
		expired_at date

table goals_timeunits:
		"Хранит связь между целями и таймюнитами"
		goal_id uuid
		timeunit_id uuid

table timeunits:
		timeunit_id uuid
		info varchar(250) # не обязательное уточнение
		start_time datetime
		end_time datetime

## таск
V Добавить Postgre
V Добавить асинхронный SQL ALCHEMY
_ Создать модели
_ Запустить и потестить таблицы в Postgre

_ Добавить Alembic

_ Добавить генератор тестовых данных
_ Написать тесты
