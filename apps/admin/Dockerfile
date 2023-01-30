FROM python:3.9-alpine3.13
LABEL maintainer="philipkogel"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /apps/admin/requirements.txt
COPY ./ /apps/admin

WORKDIR /apps/admin

EXPOSE 8004

ARG DEV=false
RUN python -m venv /py && \
  /py/bin/pip install --upgrade pip && \
  apk add --update --no-cache postgresql-client && \
  apk add --update --no-cache --virtual \
  build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
  /py/bin/pip install -r requirements.txt

ENV PATH="/py/bin:$PATH"
