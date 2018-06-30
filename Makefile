ifndef version
    version=latest
endif

DOCKER_IMAGE = hulk89/github_song:$(version)

all:
	@echo DOCKER_IMAGE = $(DOCKER_IMAGE)

build:
	docker build --rm -t $(DOCKER_IMAGE) .

push:
	docker push $(DOCKER_IMAGE)
