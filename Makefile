all: clean build

build:
    docker-compose build
	echo "Build."

clean:
	echo "Clean."
