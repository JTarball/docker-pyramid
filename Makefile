NAME=app
PACKAGE_NAME=javaab_auth

# #Calls to docker-env
DEPS=

# #Modules that need installing
# PYTHON_INSTALL=

# export PYTHON_INSTALL

all: run

cmd:
	bash -c '$(DEPS) docker-compose run --service-ports $(NAME) $(run)'

run:
	make cmd

check:
	make cmd run="py.test --cov --cov-report=term-missing"

pshell:
	make cmd run="pshell development.ini"

sniffer:
	make cmd_no_deps run=sniffer

lint:
	make cmd run="pylint $(PACKAGE_NAME)"

flake8:
	make cmd run="flake8"

shell:
	docker-compose run $(NAME) /bin/bash
