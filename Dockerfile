FROM alpine:latest

WORKDIR /app
COPY calculator .

RUN apk update && apk upgrade
RUN apk add --no-cache nodejs npm python3 py3-pip
RUN npm install

RUN python -m venv /env && \
  . /env/bin/activate && \
  pip install pytest build

ENV PATH="/env/bin:$PATH"
