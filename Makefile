build:
	python build.py

runserver:
	python -m http.server --bind 127.0.0.1 --directory . 8080
