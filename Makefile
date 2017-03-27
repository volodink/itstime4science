all: clean build

build:
	docker-compose build
	echo "Build."

clean:
	echo "Clean."

run:
	docker-compose up

rund:
	docker-compose up -d

stop:
	docker-compose stop

destroy:
	docker-compose rm -f