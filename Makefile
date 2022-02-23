setup:
	@python3 -m pip install -r requirements.txt

build-docker:
	@docker build -t voronoi .

down-docker:
	@docker-compose down --rmi local

build-run:
	@docker-compose up --build; make down-docker

run:
	@docker-compose up

.PHONY: setup
