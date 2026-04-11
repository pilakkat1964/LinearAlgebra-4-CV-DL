SHELL := /bin/bash
.PHONY: build build-heavy run shell jupyter streamlit clean

IMAGE ?= la4cvdl:dev

build:
	./scripts/container.sh build --tag $(IMAGE)

build-heavy:
	./scripts/container.sh build --heavy --tag $(IMAGE)

run:
	./scripts/container.sh run --tag $(IMAGE) -- bash

shell:
	./scripts/container.sh shell --tag $(IMAGE)

jupyter:
	./scripts/container.sh jupyter --tag $(IMAGE) --port 8888

streamlit:
	./scripts/container.sh streamlit --tag $(IMAGE) --port 8501

clean:
	./scripts/container.sh clean
