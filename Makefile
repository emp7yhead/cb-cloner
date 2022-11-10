DIR ?= ''

install:
	poetry install

ru-to-en:
	poetry run ru-to-en $(DIR)
