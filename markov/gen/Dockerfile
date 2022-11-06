FROM python:alpine

WORKDIR /usr/src/app

RUN pip install --upgrade markovify

ADD gen.py gen.py
ADD entrypoint.sh entrypoint.sh

CMD /bin/sh entrypoint.sh