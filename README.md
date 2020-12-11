![Advanced Testing with Github Actions](https://github.com/noahgift/advanced-testing-techniques/workflows/Advanced%20Testing%20with%20Github%20Actions/badge.svg)

# advanced-testing-techniques
This is a repo for doing advanced testing

## Setup Project

1. Create and source virtualenv

```bash
virtualenv ~/.advanced-testing
source ~/.advanced-testing/bin/activate
```

2. Create scaffold

```bash
touch Makefile && touch test_hello.py && touch hello.py. && requirements.txt
```

3.  Populate `Makefile`

```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py hellocli.py

all: install lint test
```

### How to debug

* Print
* pdb
* testing


### How to do more things with Github Actions

* [Github Actions Docs](https://docs.github.com/en/free-pro-team@latest/actions/guides/building-and-testing-python#specifying-a-python-version)