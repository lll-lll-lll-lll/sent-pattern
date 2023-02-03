# syntax=docker/dockerfile:1

FROM python:3.10-slim as builder

WORKDIR /src

ENV POETRY_HOME=/opt/poetry\
    PIP_DISABLE_PIP_VERSION_CHECK=on\
    POETRY_HOME="/opt/poetry"\
    # Poetryによる仮想環境の自動作成を無効
    POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential 

RUN pip install --upgrade pip \
    pip install --upgrade setuptools \
    pip install poetry

COPY ./ .
RUN poetry install --no-dev

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]