FROM alpine:latest

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add --no-cache nodejs npm python3 py3-pip

RUN python -m venv /app/venv && \
  . /app/venv/bin/activate && \
  pip install pytest build

COPY calculator .

ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT [ "/bin/sh" ]
