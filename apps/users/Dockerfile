FROM python:3.9-alpine3.13
LABEL maintainer="philipkogel"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /apps/users/requirements.txt
COPY ./ /apps/users

WORKDIR /apps/users

EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
  /py/bin/pip install --upgrade pip && \
  /py/bin/pip install -r requirements.txt

ENV PATH="/py/bin:$PATH"
