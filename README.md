# gladwellproject
Project for timetracking and goal setting in work environment

## Техническое задание
Сервис должен уметь:
- Хранить данные о потраченном времени и поставленных целях (Postgre + DjangoAdmin)
- Добавлять новые категории/активности для потраченного времени (FastAPI)

- Учитывать связь потраченного времени и целей, на которые мы тратит время (Analytics)
- Уведомлять пользователей о необходимых действиях и достигнутых целях (Notifications)
- Давать возможность полнотекстового поиска (Elastic Search)

## Запуск проекта
1. Если у вас установлен Makefile, то используйте следующую команду:
```make dev-compose```
Если нет, то используйте docker-compose:
```docker-compose up --build```

2. Test Data. If you want to create test data for our project:
		a. Start project, using docker-compose
		b. ```python3 time_api/data_generator.py```


## API
Api Docs Path http://localhost:8000/docs



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

table goals:
		"Хранит цели"
		goal_id uuid
		name varchar(250)
		description text
		created_at date
		updated_at date
		expired_at date

table timeunits:
		timeunit_id uuid
		info varchar(250) # не обязательное уточнение
		start_time datetime
		end_time datetime

API
V Make cool config
V Make endpoint for adding new users. For this endpoint i should use pydantic model for request data
V Make service that works with Users
V Make other endpoints
_ Make Pagination

Telegram Bot
_ Learn Theory
_ 

gRPC API
