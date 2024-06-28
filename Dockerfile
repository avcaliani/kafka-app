FROM python:3.11

# PYTHONUNBUFFERED enables you to see your Python logs (prints) in the Docker Logs.
# If not set, you may not see them.
# More Details: https://stackoverflow.com/a/59812588
ENV POETRY_VERSION="1.8.2" \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONUNBUFFERED=1

# Adding Poetry Bin to Path
ENV PATH="/root/.local/bin:$PATH"

# Services Configuration
ENV APP_KAFKA_HOST="kafka:29092"

WORKDIR /opt/app

# 👇 Poetry
RUN apt-get update \
    && apt-get install -y build-essential python3-dev python3-setuptools curl \
    && pip install --upgrade --no-cache-dir pip \
    && curl -sSL https://install.python-poetry.org | python - --version "$POETRY_VERSION"

# 👇 Adding Files
ADD . .

# 👇 Installing project dependencies
RUN poetry install --no-dev
