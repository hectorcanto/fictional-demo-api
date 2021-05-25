PKGNAME=fictional

GREEN="\\e[32m"
REGULAR="\\e[39m"
RED="\\e[91m"

help: ## Prompts help for every command
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

shell: ## Open a ipython Django shell
	python manage.py shell -i ipython

plus:  ## Open a Django Shell Plus terminal
	@python manage.py shell_plus

clean-py: ##
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '*.pyc' -delete
	@find . -name '*.pyo' -delete

black:  ## Reformat code black-style, ignores migrations
	black -l 100 --exclude 00* ${PKGNAME}

flake:  ## Pass style check with Flake8, prompting something if everything ok
	@ flake8 \
	&& echo -e "${GREEN}Passed Flake8 style review.${REGULAR}" \
	|| (echo -e "${RED}Flake8 style review failed.${REGULAR}" ; exit 1)

linting:  ## Pass pylint linter, check setup.cfg for conf details
	@pylint --rcfile=setup.cfg ${PKGNAME}/ tests/ | tee .coverage-reports/pylint.txt

# Django
check: urls ## Check the status of the project
	@python manage.py check

migrations:  ## Make pending Django migrations
	@python manage.py makemigrations fictional sales vehicles


apply-migrations:  ## Apply pending migrations
	@python manage.py migrate

resetdb:  ## Reset the DB, will need to create tables again
	@python3 manage.py reset_db

urls:  ## Show active Django urls
	@python3 manage.py show_urls

run:  ## Launch the local server
	@python3 manage.py runserver 8000

test:  ##Launch test
	@PYTHONBREAKPOINT='IPython.core.debugger.set_trace' pytest

current-test:  ## Launch current test with ipython debugger and no stdout capture
	@PYTHONBREAKPOINT='IPython.core.debugger.set_trace' pytest -m current -s

# Other
tree:  ## Show the structure
	@tree -d -L 2

diagrams:
	@python docs/diagrams/iter1.py
	@python docs/diagrams/iter1.py
	@echo "${GREEN}Created diagrams available at docs/diagrams ${REGULAR}"

.PHONY: shell plus clean-py black flake linting cheeck migrations apply-migrations resetdb urls run test current-tests tree
