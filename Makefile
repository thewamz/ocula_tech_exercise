SHELL := /bin/bash

USER_ID := $(shell id -u)
GROUP_ID := $(shell id -g)
APP_NAME := ocula
APP_VERSION := $(shell git describe --tags --dirty --always)
# APP_VERSION := 1.0.0
CURRENT_UNIX_EPOCH_TIMESTAMP := $(shell date +%s)
POSTGRES_VERSION=16.0

DB_USER=postgres
DB_PASSWORD=postgres
DATABASE_URL=postgres://$(DB_USER):$(DB_PASSWORD)@db/$(APP_NAME)

.PHONY: all
all: build

.PHONY: build-image
build-image:
	@echo "[Building image with build time]"
	docker build \
	--build-arg APP_VERSION=$(APP_VERSION) \
	--build-arg BUILD_TIME=$(CURRENT_UNIX_EPOCH_TIMESTAMP) \
	--tag $(APP_NAME):$(APP_VERSION) .

.PHONY: build
build:
	@echo "[Building image]"
	docker build \
	--build-arg APP_VERSION=$(APP_VERSION) \
	--tag $(APP_NAME):$(APP_VERSION) .

.PHONY: up
up: build
	@echo "[Bringing up a dev environment]"
	UID=$(USER_ID) \
	APP_VERSION=$(APP_VERSION) \
	DATABASE_URL=$(DATABASE_URL) \
	docker-compose up --remove-orphans -d

.PHONY: up-prod
up-prod: build
	@echo "[Bringing up a prod like environment]"
	UID=$(USER_ID) \
	APP_VERSION=$(APP_VERSION) \
	DATABASE_URL=$(DATABASE_URL) \
	docker-compose -f docker-compose.prod.yml up --remove-orphans -d

.PHONY: down
down:
	docker-compose down

.PHONY: down-prod
down-prod:
	@echo "[Bringing down a prod like environment]"
	docker-compose -f docker-compose.prod.yml down

.PHONY: build-dists
build-dists:
	tox -e build-dists

.PHONY: test
test: build
	@echo "[Running unit tests]"
	docker pull postgres:$(POSTGRES_VERSION)

	$(eval POSTGRES_CONTAINER := $(shell \
	docker run \
	-e POSTGRES_DB=$(APP_NAME) \
	-e POSTGRES_USER=$(DB_USER) \
	-e POSTGRES_PASSWORD=$(DB_PASSWORD) \
	-p 5433:5433 \
	-d postgres:$(POSTGRES_VERSION)))

	docker run --rm --user "$(USER_ID):$(GROUP_ID)" \
	-e DATABASE_URL=$(DATABASE_URL) \
	-e DJANGO_SETTINGS_MODULE="ocula.settings.docker" \
	-e TIMESTAMP_SIGNER_SALT="salt" \
	-v "$$(pwd)/testdata:/code/testdata" \
	-v "$$(pwd)/static:/code/static" \
	-v "$$(pwd)/media:/code/media" \
	--link $(POSTGRES_CONTAINER):db \
	$(APP_NAME):$(APP_VERSION) \
	./manage.py test --parallel \
	|| (echo "docker rm -f [postgres]" \
	&& docker rm -f $(POSTGRES_CONTAINER) && false)

	@echo "docker rm -f [postgres]"
	docker rm -f $(POSTGRES_CONTAINER)

.PHONY: check
check:
	@echo "[Running QA checks]"
	tox -e checkqa

.PHONY: requirements
requirements:
	@echo "Generate requirements.txt using pip tools"
	pip-compile --generate-hashes --build-isolation --allow-unsafe requirements.in

.PHONY: upgrade-requirements
upgrade-requirements:
	@echo "Generate requirements.txt using pip tools"
	pip-compile --upgrade --generate-hashes --build-isolation --allow-unsafe \
	requirements.in
