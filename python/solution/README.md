# QuickBase Interview Demo

## Prerequisites

You need to have [Docker CE](https://docs.docker.com/install/ "Install Docker CE") and [Docker
Compose](https://docs.docker.com/compose/install/ "Install Docker Compose") installed.

If your environment is other than GNU/Linux, there may be some differences in the interaction with
Docker, so please follow the [Docker documentation](https://docs.docker.com/ "Docker documentation")
if something doesn't suits you.


## Setup Local Docker Environment

Under `python/solution/environment` you'll find all the configuration files, you need to run the
project on docker.

To prepare your environment, you need to cd `python/solution/environment` and:
- Sync the `.env.tmpl` file to `.env` and add your API keys.
- run `$ docker-compose up --build`

That's all!

NB!: It is good to always run `docker-compose up` with the `--build` option to keep the requirements
in sync. If a colleague of you changes the python requirements and you omit the `--build` option,
you will be in trouble. The build uses cache, so it is cheap to do it.


## Utility scripts

To run all the linters and tests, you have two options:

1. Enter the Docker container and exec the script:
  - `$ cd python/solution/environment`
  - `$ docker-compose exec app bash`
  - `$ cd python/solution/`
  - `$ ./run_checks.py --help`

2. Run this one liner:
  - `$ cd python/solution/environment`
  - `$ docker-compose exec app bash -c "cd python/solution/ && ./run_checks.py --help"`

To be able to use git and gitlint inside docker, we need to mount the root of our project. This is
why we need to always type the full path to our scripts.


## Basic conventions

To keep things clean, we use:
- [gitlint](https://jorisroovers.com/gitlint/ "gitlint documentation") to keep eye on our commit
  messages. See the .gitlint file for our custom rules.
- [flake8](https://flake8.pycqa.org/en/latest/index.html "flake8 documentation") to keep our code
  clean. See the .flake8 file for our custom rules.
- [mypy](https://mypy.readthedocs.io/en/stable/ "mypy documentation") to check our types statically.
