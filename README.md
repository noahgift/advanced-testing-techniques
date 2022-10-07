
Just Python 3.8

![Advanced Testing with Github Actions](https://github.com/noahgift/advanced-testing-techniques/workflows/Advanced%20Testing%20with%20Github%20Actions/badge.svg)

Python 3.6-3.8 + PyPi

![Python package](https://github.com/noahgift/advanced-testing-techniques/workflows/Python%20package/badge.svg)

Ubuntu + OS X Python 3.6-3.8 + PyPi

![Python package](https://github.com/noahgift/advanced-testing-techniques/workflows/Python%20package/badge.svg)


Code Climate Maintability

[![Maintainability](https://api.codeclimate.com/v1/badges/dcd577eb79e75a4798c3/maintainability)](https://codeclimate.com/github/noahgift/advanced-testing-techniques/maintainability)

Code Climate Test Coverage

[![Test Coverage](https://api.codeclimate.com/v1/badges/dcd577eb79e75a4798c3/test_coverage)](https://codeclimate.com/github/noahgift/advanced-testing-techniques/test_coverage)

AWS Code Build

![AWS Badge](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiR0lIc1B2R0RBNHlrUldxKzZCSlRhalRvK1FodkJKWGs2aXRRWkNlMWdnZGFUMDhyODJkMVlNTXVmTjV3aHlIQTdkOHdneUhUQi9NUGtoZFlTYnFxNy9VPSIsIml2UGFyYW1ldGVyU3BlYyI6ImRBdzBBTGpsSzBVMGtSUmwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

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
