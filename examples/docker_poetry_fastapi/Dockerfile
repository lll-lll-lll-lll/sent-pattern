# syntax=docker/dockerfile:1

FROM python:3.10-slim

WORKDIR /src

ENV POETRY_HOME=/opt/poetry\
    PIP_DISABLE_PIP_VERSION_CHECK=on\
    POETRY_HOME="/opt/poetry"\
    POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
    && apt-get install --no-install-recommends -y 

RUN pip install --upgrade pip \
    pip install --upgrade setuptools \
    pip install poetry

COPY ./ .
RUN poetry install --no-dev

EXPOSE 80

CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "80"]