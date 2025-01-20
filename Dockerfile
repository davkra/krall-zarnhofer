FROM python:3.10.12

WORKDIR /calculator

COPY calculator .

RUN pip install pytest build

ENTRYPOINT [ "/bin/bash" ]
