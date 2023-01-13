FROM python:3.9-alpine3.13
LABEL maintainer="philipkogel"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /apps/email/requirements.txt
COPY ./apps/email /apps/email

WORKDIR /apps/email

EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
  /py/bin/pip install --upgrade pip && \
  /py/bin/pip install -r requirements.txt

ENV PATH="/py/bin:$PATH"
