FROM python:3

WORKDIR /usr/src/app

RUN pip install --upgrade markovify spacy nltk
RUN python -m spacy download en_core_web_sm

ADD train.py train.py
ADD entrypoint.sh entrypoint.sh

CMD /bin/sh entrypoint.sh