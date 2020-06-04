# FunBox test task
## Install packages into env
This task is implemented in Python 3.7 using the FastAPI framework.
To start clone this repo in working directory, make virtual environment and activate it.
```
$ python3.7 -m venv env
$ source env/bin/activate
```
Next, you need to install all dependent packages.
```
$(env) pip install -r requirements.txt
```
## Install Redis Server
You can install Redis using official documentation.
[Redis Install](https://redis.io/topics/quickstart)

## Configuration
Config file - redis_config.yaml
You can change the config and add your own host, port and database number to connect with Redis server.
```
redis_config.yaml

# Set Redis host, port and DB number
    host: localhost
    port: 6379
    db: 1
```
## Unit Tests
To check Redis server connection run:
```
$(env) python funbox_task/tests.py
```
If one of the tests fails, check the yaml file and your Redis Server configuration.

## Start
To start App run:
```
$(env) funbox_task/ uvicorn main:api --reload
```
## Api Docs
To check API Docs visit:
(http://<your_domain_or_ip>/docs)





