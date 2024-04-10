task=2

start: stop
	@docker-compose -f=homework_$(task)/docker-compose.yaml -p homework_$(task) up -d

start_with_rebuild: stop
	@docker-compose -f=homework_$(task)/docker-compose.yaml -p homework_$(task) up -d --rebuild

stop:
	@docker-compose -p homework_$(task) down

exec:
	@docker exec -it app_homework_$(task) bash