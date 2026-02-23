IMAGE_NAME=ghcr.io/$(GITHUB_USER)/latex-ci
TAG=latest
TEX_FILE=resume.tex

.PHONY: docker-build docker-push compile clean

docker-build:
	docker build -t $(IMAGE_NAME):$(TAG) .

docker-push:
	docker push $(IMAGE_NAME):$(TAG)

compile:
	pdflatex -interaction=nonstopmode $(TEX_FILE)
	test -f resume.pdf

clean:
	pdflatex -c $(TEX_FILE)