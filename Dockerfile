FROM python:3.9
LABEL maintainer = "kevinha298"

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
COPY ./app /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app-user

ENV PATH="/py/bin:$PATH"

USER app-user