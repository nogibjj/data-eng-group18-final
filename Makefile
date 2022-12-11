install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest test*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

all:
	make install test format lint