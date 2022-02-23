setup:
	@python3 -m pip install -r requirements.txt

build-docker:
	@docker build -t voronoi .

build-run:
	@docker-compose up --build; docker-compose down --rmi local

run:
	@docker-compose run --rm

.PHONY: setup
