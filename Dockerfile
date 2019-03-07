FROM python:3.7-alpine

RUN apk --no-cache --update add \
  gcc \
  musl-dev

RUN mkdir /source
WORKDIR /source

COPY statuspageio statuspageio
COPY setup.py setup.py

RUN pip install -e .[dev]

ENTRYPOINT ["sh", "entrypoint.sh"]
