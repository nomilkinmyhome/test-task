# Test task

### Run project

1. ```cp config.yaml.example config.yaml```
2. ```cp mysql.cnf.example mysql.cnf```
3. ```make start```
4. ```make migrate```

**You should manually add some data to the DB tables.<br>**
**Use credentials from mysql.cnf.example.**

### Other commands

1. Start: ```make start```
2. Stop: ```make down```
3. Make migrations: ```make migrations```
4. Migrate: ```make migrate```
5. Run linters: ```make fmt```

### Task description

Develop REST API server using django-rest-framework with pagination, sorting and filtering for two models:

Transaction (id, wallet_id (fk), txid, amount);

Wallet (id, label, balance);

Where txid is required unique string field, amount is a number with 18-digits precision, label is a string field, balance is a summary of all transactions’s amounts. Transaction amount may be negative. Wallet balance should NEVER be negative

Tech Stack:

Python – 3.11+
Database – mysql
API specification – JSON:API — A specification for building APIs in JSON (you are free to use plugin https://django-rest-framework-json-api.readthedocs.io/en/stable/)

Will be your advantage:

Test coverage
SQLAlchemy migrations is an option
Any linter usage
Quick start app guide if you create your own docker-compose or Dockerfiles
Comments in non-standart places in code
Use database indexes if you think it's advisable
Leave github link to repo. Please delete the repo after HR feedback

[execution time limit] 4 seconds (sh)

[memory limit] 1 GB