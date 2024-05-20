# ⚙️ Dev Setup

![License](https://img.shields.io/github/license/avcaliani/kafka-app?logo=apache&color=lightseagreen)

In this document you will find the step by step to prepare your setup to execute this repository code.

## 📝 Requirements

To execute this project you will need some softwares installed.

- [Docker] 🐋
- Python 3.8 or Higher (in my case I use [pyenv]) 🐍
- [Poetry] 📦

[Docker]: https://www.docker.com/
[pyenv]: https://github.com/pyenv/pyenv
[Poetry]: https://python-poetry.org/

## 🪜 Step by Step

To execute the following steps, it is important to be in the project root directory.

### Kafka Setup

In this section we are going up a **local** Kafka.

```bash
# Build & Up
docker compose build && docker compose up -d

# Shutting Down
docker compose down
```

**Do you want to test this Kafka via CLI?**  
I created this document 👉 [Kafka on CLI](../kafka/README.md) 👈 with some nice commands for you to try 🤓

### Development Setup

Now, let's see how to prepare your development environment.

```bash
# Optional Step 👇
pyenv local 3.11.6

# Creating Python virtual env 👇
python3 -m venv .venv \
    && source .venv/bin/activate \
    && pip install --upgrade pip

# Installing project dependencies 👇
poetry install
```

### The End

**That's all folks 🍻**  
Now, go back to the project's README and continue your journey on the "[How do I execute this project?]" topic.

[How do I execute this project?]: ../README.md#how-do-i-execute-this-project
