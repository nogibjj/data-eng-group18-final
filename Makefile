install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest test*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

deploy: 
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/b3t7f7d0
	docker build -t test2 .
	docker tag test2:latest public.ecr.aws/b3t7f7d0/test2:latest
	docker push public.ecr.aws/b3t7f7d0/test2:latest
	
all:
	make install test format lint