# Celery Test
This repository contains some sample code to investigate the overhead of Celery.
To be specific, it tries to answer the following questions:
1. What is the overhead of scheduling Celery tasks? Where does this depend on?
2. Does Celery prioritization work, and how does it work?

## Installation
This project can be installed with the following command:
```bash
poetry install
```

### Running celery
Celery can be started with the following command:
```bash
# Make sure the poetry environment is active
$(which celery) -A celery_test.app:app worker -Q tasks --loglevel info
```

## Tests
Tests are made using `pytest`.
They are made to show several usages on how celery can be used. 
Also, tests are designed to answer the questions above.