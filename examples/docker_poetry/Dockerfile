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
    build-essential \
    git \
    cmake 

RUN pip install --upgrade pip \
    pip install --upgrade setuptools \
    pip install poetry

COPY ./ .
RUN poetry install


RUN mv internal/ /usr/local/lib/python3.10/site-packages

RUN python -m compileall main.py && mv __pycache__/main.cpython-310.pyc ./

CMD ["python","main.cpython-310.pyc"]

###
# Deploy
###
FROM python:3.10-slim as prod

WORKDIR /src

COPY --from=builder /usr/local/lib/python3.10/site-packages /root/.local/lib/python3.10/site-packages

COPY --from=builder ./src/main.cpython-310.pyc ./src

EXPOSE 50051

CMD ["python", "main.cpython-310.pyc"] 