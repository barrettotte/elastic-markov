FROM python:alpine

WORKDIR /usr/src/app

RUN pip install --upgrade markovify random-username

COPY gen.py gen.py
COPY entrypoint.sh entrypoint.sh

CMD /bin/sh entrypoint.sh
