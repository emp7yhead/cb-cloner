DIR ?= 'code-basics/exercises-python/'

install:
	poetry install

ru-to-en:
	poetry run ru-to-en $(DIR)
