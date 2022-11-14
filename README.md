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

table users_goals:
		user_id
		goal_id

table goals:
		"Хранит цели"
		goal_id uuid
		user_id
		name varchar(250)
		description text
		category_id

table timeunits:
		timeunit_id uuid
		info varchar(250) # не обязательное уточнение
		length int  # речь про минуты длительности активности



table timeunits_goals:
		timeunit_id uuid
		goal_id uuid
