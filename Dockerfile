FROM python:3.11

# PYTHONUNBUFFERED enables you to see your Python logs (prints) in the Docker Logs.
# If not set, you may not see them.
# More Details: https://stackoverflow.com/a/59812588
ENV POETRY_VERSION="1.8.4" \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONUNBUFFERED=1

# Services Configuration
ENV APP_KAFKA_HOST="kafka-dev:29092"

WORKDIR /opt/app

# 👇 Poetry
# https://python-poetry.org/docs/#ci-recommendations
RUN apt-get update \
    && apt-get install -y build-essential python3-dev python3-setuptools curl \
    && pip install --upgrade --no-cache-dir pip

RUN python -m venv "$POETRY_HOME" \
    && "$POETRY_HOME/bin/pip" install poetry=="$POETRY_VERSION" \
    && "$POETRY_HOME/bin/poetry" --version

# 👇 Adding Files
ADD . .

# 👇 Installing project dependencies
RUN "$POETRY_HOME/bin/poetry" install --no-dev
