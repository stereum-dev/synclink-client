# SyncLink Client

![GitHub - SyncLink - ReadMe](https://raw.githubusercontent.com/wiki/stereum-dev/synclink-spec/images/SyncLink-1130x420.png)

---

[![IE](https://img.shields.io/badge/Website-0076D6?style=for-the-badge&logo=Internet%20Explorer&logoColor=white)](https://synclink.io/) [![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/8Znj8K6GjN)
[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/stereumdev)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/channel/UCq_LYa0idkQcSnxBUmiJm3Q)
[![Gmail](https://img.shields.io/badge/EMail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:synclink@synclink.io)

[![Build Status](https://img.shields.io/github/workflow/status/stereum-dev/synclink-client/docker?color=blue)](https://github.com/stereum-dev/synclink-client/actions/workflows/docker.yaml)
[![Latest Release](https://img.shields.io/github/release/stereum-dev/synclink-client?color=blue)](https://github.com/stereum-dev/synclink-client/releases/latest)
![GitHub](https://img.shields.io/github/license/stereum-dev/synclink-client?color=blue)
[![Discord](https://img.shields.io/discord/769190437050122311?color=blue&label=discord)](https://discord.gg/8Znj8K6GjN)
[![GitPOAPs](https://public-api.gitpoap.io/v1/repo/stereum-dev/synclink-client/badge)](https://www.gitpoap.io/gh/stereum-dev/synclink-client)

Python implementation of the [SyncLink Client](https://github.com/stereum-dev/synclink-spec/wiki/SyncLink-Client). See the [Changelog](https://github.com/stereum-dev/synclink-client/releases) for details of the latest releases and upcoming changes.

# WARNING

**CURRENTLY IN DEVELOPMENT - DO NOT USE IN PRODUCTION!**

You can use the SyncLink Client as described in this document however during development we continue implementing changes that could (and very likely will) make some or all of the described operations and tasks below obsolete.

# Table of Contents

- [Supported clients](#supported-clients)

* [Usage](#usage)
  - [Configuration](#configuration)
    - [Options](#options)
    - [Config file](#config-file)
    - [Command line arguments](#command-line-arguments)
    - [Environment variables](#environment-variables)
  - [Getting Started](#getting-started)
    - [Run with Docker](#run-with-docker)
      - [Images](#images)
      - [Quick start with Docker](#quick-start-with-docker)
    - [Run from source](#run-from-source)
      - [Quick start from source on Windows](#quick-start-from-source-on-windows)
      - [Quick start from source on Linux and macOS](#quick-start-from-source-on-linux-and-macos)

- [Contributing](#contributing)
  - [Unit Testing and Linting](#unit-testing-and-linting)

* [Contact](#contact)

- [Docker Examples](#docker-examples)
  - [Production Container Examples](#production-container-examples)
    - [Start container from image with "run" command and "config file"](#docker-example-prod-run-cfg)
    - [Start container from image with "run" command and "command line arguments"](#docker-example-prod-run-args)
    - [Start container from image with "run" command and "environment variables"](#docker-example-prod-run-env)
    - [Start container from image with "compose" command](#docker-example-prod-compose)
  - [Development Container Examples](#development-container-examples)
    - [Start container from build-image with "run" command and "config file"](#docker-example-dev-run-cfg)
    - [Start container from build-image with "run" command and "command line arguments"](#docker-example-dev-run-args)
    - [Start container from build-image with "run" command and "environment variables"](#docker-example-dev-run-env)
    - [Start container from build-image with "compose" command](#docker-example-dev-compose)

# Supported clients

| Client     | Support |
| ---------- | ------- |
| Lighthouse | ✅      |
| Lodestar   | ✅      |
| Nimbus     | ✅      |
| Prysm      | ✅      |
| Teku       | ✅      |

# Usage

There are multiple ways you can configure and run the SyncLink Client application. While [the recommended setup for production environments is Docker](#run-with-docker), it is also possible to [run the app directly from source with Python](#run-from-source), which is mostly preferred for development on your local system, however also an absolutely valid setup for production.

## Configuration

The SyncLink Client [options](#options) must be configured either thru a yaml [config file](#config-file), [command line arguments](#command-line-arguments) or [environment variables](#environment-variables).

### Options

| Name   | Default                 | Required | Description                                                                         |
| ------ | ----------------------- | -------- | ----------------------------------------------------------------------------------- |
| addr   | 0.0.0.0                 | No       | The IP address or domain where the SyncLink Client is listening for new connections |
| port   | 9000                    | No       | The port where the SyncLink Client is listening for new connections                 |
| nodes  | [http://localhost:8000] | No       | List of URLs to your SyncLink Server Nodes                                          |
| config | config.yaml             | No       | Path to a yaml config file                                                          |

### Config file

By default the SyncLink Client attempts to read the configuration from `config.yaml`. The path to this file can however explicitly specified by [command line arguments](#command-line-arguments) or [environment variables](#environment-variables). The configuration management also supports a hierarchical config structure, which means you can optionally add the ["_config_" option](#options) within a config file to load additional settings from a separate config file.

Example `config.yaml` (see [config.yaml.example](./config.yaml.example)):

```
port: 9000
nodes:
  - http://localhost:8000
  - http://host.docker.internal:8000
```

### Command line arguments

You can also configure the SyncLink Client [options](#options) on the command line. Command line arguments will overwrite all identical [options](#options) that are already defined in the [config file](#config-file) and you can of course set the path to the [config file](#config-file) itself.

By default command line arguments must be prefixed with "--" and always lowercase.
For example, to specify `addr` as command line argument:

```
python main.py --addr="127.0.0.1"
```

> In most cases it is also possible to use just a shortcut, run `python main.py -h` for details.

### Environment variables

At last you can configure the SyncLink Client [options](#options) by environment variables. They are especially useful with the Docker Image and have the highest priority in the configuration tree.

Environment variables must be prefixed with "**SYLI\_**" and always **UPPERCASE**.
For example, to specify `addr` as environment variable:

```
export SYLI_ADDR="127.0.0.1"
python main.py
```

will be converted to `python main.py --addr "127.0.0.1"`.

For lists, the environment variables need additionally suffixed with a number, e.g.:

```
export SYLI_NODE_1="10.0.0.1"
export SYLI_NODE_2="10.0.0.2"
python main.py
```

will be converted to `python main.py --node "10.0.0.1" --node "10.0.0.2"`.

If you have accidentally specified an environment variable that is not supported (see [options](#options)), you need to unset the variable to avoid an error. For example:

```
export SYLI_BLA="12345"
python main.py
```

will be converted to `python main.py --bla "12345"`.

This will of course result in the error `main.py: error: unrecognized arguments: --bla 12345`.

Therefore, you'd have to remove the environment variable:

```
unset SYLI_BLA
```

## Getting started

The recommended setup for production environments is to [run the SyncLink Client with Docker](#run-with-docker) but it is also possible to [run the SyncLink Client directly from source with Python](#run-from-source). Make sure you've read the [configuration section](#configuration) and then you're good to go.

### Run with Docker

1. If not already done, [install Docker](https://docs.docker.com/get-docker/) on your OS.
2. Pull the SyncLink Client Docker Image ([stereum/synclink-client](https://hub.docker.com/r/stereum/synclink-client/tags)) from Docker Hub and follow the [quick start with Docker](#quick-start-with-docker) or one of the [more advanced Docker examples](#docker-examples) on bottom.

#### Images

- `latest` - latest release of the SyncLink Client on python:3.10-slim
- `$version` - specific release (e.g.: `v0.0.1`) of the SyncLink Client on python:3.10-slim

#### Quick start with Docker

```
docker run --name synclink-client --rm -it -p "9000:9000" -e SYLI_NODE_1="$YOUR_SYNCLINK_SERVER_URL" stereum/synclink-client
```

**Important**

Change `$YOUR_SYNCLINK_SERVER_URL` to the URL of your SyncLink Server API (e.g: `http://localhost:8000` or `http://host.docker.internal:8000` if the server is running in a Docker container on your local machine).

After the app is started you can visit the API docs (depending on your [config](#configuration)) by default at <http://127.0.0.1:9000/docs>.

If you're done you can stop the Docker container by typing `CTRL+C` in your active terminal.

### Run from source

1. Download a release from the [releases page](https://github.com/stereum-dev/synclink-client/releases) (or clone the GitHub repository).
2. Refer to the [official Python docs](https://www.python.org/doc/) to install [Python >= 3.10](https://www.python.org/downloads/) on your OS.
3. On Debian or Ubuntu run `apt install pythonX.Y-venv` to install venv. (Replace `X.Y` with the python MAJOR and MINOR version retrieved by `python -V`)
4. Extract the release (or continue directly with step #5 if you just cloned the GitHub repository).
5. Follow the quick start from source on [Windows](#quick-start-from-source-on-windows) or [Linux and macOS](#quick-start-from-source-on-linux-and-macos) examples.

#### Quick start from source on Windows

```
python -m venv .venv
".venv/scripts/activate.bat"
pip install -r requirements.txt
python main.py --addr="$YOUR_SYNCLINK_SERVER_URL"
```

#### Quick start from source on Linux and macOS

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py --addr="$YOUR_SYNCLINK_SERVER_URL"
```

**Important**

Change `$YOUR_SYNCLINK_SERVER_URL` to the URL of your SyncLink Server API (e.g: `http://localhost:8000` or `http://host.docker.internal:8000` if the server is running in a Docker container on your local machine).

After the app is started you can visit the API docs (depending on your [config](#configuration)) by default at <http://127.0.0.1:9000/docs>.

If you're done you can stop the Python process and deactivate the virtual environment by typing the following in your active terminal:

```
CTRL+C
deactivate
```

# Contributing

Contributions are greatly appreciated and pull requests will be reviewed/merged ASAP!

If you're interested in improving the SyncLink Client please follow these steps:

1. Fork the project
2. Create your feature branch:
   - `git checkout -b feat/new-feature`
3. Commit your changes:
   - `git commit -m "feat(optional): new feature"`
4. Push the branch: -`git push origin feat/new-feature`
5. Open a pull request

> Note: To test your changes in a local Docker container see the [Development Container Examples](#development-container-examples).

### Unit Testing and Linting

All pull requests running thru automated tests. It is recommended to run these tests locally before you open a pull request.

- Setup your local development environment, thus you're able to [run from source](#run-from-source)
- Execute `pytest` to run Unit Tests (where no errors as result means passed)
- Execute `flake8` to run Lint Tests (where 0 as result means passed)

# Contact

[![Discord](https://img.shields.io/discord/769190437050122311?color=blue&label=discord)](https://discord.gg/8Znj8K6GjN)

To get in touch just [join the Stereum Discord server](https://discord.gg/8Znj8K6GjN) and leave a message in one of the public channels or drop us an email to [synclink@synclink.io](mailto:synclink@synclink.io). We are happy to get your feedback!

# Docker Examples

Below you'll find a few practical examples of how to start and stop the SyncLink Client with `docker run` or `docker compose` commands.
Keep in mind that these examples should just give you a hint - it is absolutely your freedom of choice how to run the SyncLink Client!
For more details regarding Docker just visit [https://docs.docker.com](https://docs.docker.com/).

**Generic description of the used Docker commands**

| Command                                                                                  | Description                          |
| ---------------------------------------------------------------------------------------- | ------------------------------------ |
| [docker rm](https://docs.docker.com/engine/reference/commandline/rm)                     | Remove one or more containers        |
| [docker run](https://docs.docker.com/engine/reference/commandline/run)                   | Run a command in a new container     |
| [docker logs](https://docs.docker.com/engine/reference/commandline/logs)                 | Fetch the logs of a container        |
| [docker stop](https://docs.docker.com/engine/reference/commandline/stop)                 | Stop one or more running containers  |
| [docker compose up](https://docs.docker.com/engine/reference/commandline/up)             | Create and start containers          |
| [docker compose pull](https://docs.docker.com/engine/reference/commandline/pull)         | Pull service images                  |
| [docker compose down](https://docs.docker.com/engine/reference/commandline/compose_down) | Stop and remove containers, networks |

> See also [https://docs.docker.com/engine/reference/commandline](https://docs.docker.com/engine/reference/commandline)

**Important**

Change `$YOUR_SYNCLINK_SERVER_URL` to the URL of your SyncLink Server API (e.g: `http://localhost:8000` or `http://host.docker.internal:8000` if the server is running in a Docker container on your local machine).

After the app is started you can visit the API docs (depending on your [config](#configuration)) by default at <http://127.0.0.1:9000/docs>.

## Production Container Examples

<a name="docker-example-prod-run-cfg"></a>

#### Start container from [stereum/synclink-client](https://hub.docker.com/r/stereum/synclink-client/tags) image with `run` command and [config file](#config-file)

Copy [config.yaml.example](./config.yaml.example) to `config.yaml` and [configure](#configuration) as needed, then:

```
docker rm --force synclink-client
docker run -d --name synclink-client --rm -it -p 9000:9000 -v $(pwd)/config.yaml:/opt/synclink-client/config.yaml stereum/synclink-client
docker logs -f synclink-client
docker stop synclink-client
```

<a name="docker-example-prod-run-args"></a>

#### Start container from [stereum/synclink-client](https://hub.docker.com/r/stereum/synclink-client/tags) image with `run` command and [command line arguments](#command-line-arguments)

```
docker rm --force synclink-client
docker run -d --name synclink-client --rm -it -p 9000:9000 stereum/synclink-client python main.py --node="$YOUR_SYNCLINK_SERVER_URL"
docker logs -f synclink-client
docker stop synclink-client
```

<a name="docker-example-prod-run-env"></a>

#### Start container from [stereum/synclink-client](https://hub.docker.com/r/stereum/synclink-client/tags) image with `run` command and [environment variables](#environment-variables)

```
docker rm --force synclink-client
docker run -d --name synclink-client --rm -it -p "9000:9000" -e SYLI_NODE_1="$YOUR_SYNCLINK_SERVER_URL" stereum/synclink-client
docker logs -f synclink-client
docker stop synclink-client
```

<a name="docker-example-prod-compose"></a>

#### Start container from [stereum/synclink-client](https://hub.docker.com/r/stereum/synclink-client/tags) image with `compose` command

Copy [docker-compose.yaml.example](./docker-compose.yaml.example) to `docker-compose.yaml` and [configure](#configuration) as needed, then:

```
docker rm --force synclink-client
docker-compose pull
docker-compose --project-name synclink-client up -d
docker logs -f synclink-client
docker-compose --project-name synclink-client down
```

## Development Container Examples

<a name="docker-example-dev-run-cfg"></a>

#### Start container from `dev/synclink-client` build-image with `run` command and [config file](#config-file)

Copy [config.yaml.example](./config.yaml.example) to `config.yaml` and [configure](#configuration) as needed, then:

```
docker build --tag dev/synclink-client .
docker rm --force dev-synclink-client
docker run -d --name dev-synclink-client --rm -it -p 9000:9000 -v $(pwd)/config.yaml:/opt/synclink-client/config.yaml dev/synclink-client
docker logs -f dev-synclink-client
docker stop dev-synclink-client
```

<a name="docker-example-dev-run-args"></a>

#### Start container from `dev/synclink-client` build-image with `run` command and [command line arguments](#command-line-arguments)

```
docker build --tag dev/synclink-client .
docker rm --force dev-synclink-client
docker run -d --name dev-synclink-client --rm -it -p 9000:9000 dev/synclink-client python main.py --node="$YOUR_SYNCLINK_SERVER_URL"
docker logs -f dev-synclink-client
docker stop dev-synclink-client
```

<a name="docker-example-dev-run-env"></a>

#### Start container from `dev/synclink-client` build-image with `run` command and [environment variables](#environment-variables)

```
docker build --tag dev/synclink-client .
docker rm --force dev-synclink-client
docker run -d --name dev-synclink-client --rm -it -p "9000:9000" -e SYLI_NODE_1="$YOUR_SYNCLINK_SERVER_URL" dev/synclink-client
docker logs -f dev-synclink-client
docker stop dev-synclink-client
```

<a name="docker-example-dev-compose"></a>

#### Start container from `dev/synclink-client` build-image with `compose` command

Copy [docker-compose.dev.yaml.example](./docker-compose.dev.yaml.example) to `docker-compose.dev.yaml` and [configure](#configuration) as needed, then:

```
docker rm --force dev-synclink-client
docker-compose --project-name dev-synclink-client -f docker-compose.dev.yaml up -d
docker logs -f dev-synclink-client
docker-compose --project-name dev-synclink-client down
```
