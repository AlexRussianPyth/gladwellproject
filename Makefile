dev-compose:
	docker-compose -f docker-compose.dev.yml up --build
dev-api:
	python3 time_api/main.py

