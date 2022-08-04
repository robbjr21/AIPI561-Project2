install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


format:
	black *.py


lint:
	pylint --disable=R,C,W0702 main_methods.py

all: install lint test
