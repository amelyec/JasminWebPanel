REGISTRY=local
IMAGE_NAME=$(REGISTRY)/jasminwebpanel
VERSION=master

default: help

help:
	@echo "JasminWebPanel: A docker wrapper for the jasminwebpanel"
	@echo ""
	@echo "Usage:"
	@echo "    make build-docker            build the docker image"
	@echo "    make run-dev                 run the dev "
	@echo ""
	@echo "Authors:"
	@echo "    See https://github.com/tarikogut/JasminWebPanel"


build-docker:
	docker build --rm -t $(IMAGE_NAME):$(VERSION) ./

run-dev:
	docker run --net=zdeploystack_default -p 8000:8000 -e DB_ENGINE=postgres -e DB_HOST=postgres \
	 -e DB_USER=airflow -e DB_PASSWORD=airflow \
	 -e JASMIN_HOST=jasmin -e JASMIN_PORT=8990 -e JASMIN_USERNAME=jcliadmin -e JASMIN_PASSWORD=jclipwd \
	 -it $(IMAGE_NAME):$(VERSION)