FROM python:3

WORKDIR /usr/src/app

COPY train.py train.py
COPY entrypoint.sh entrypoint.sh

RUN pip install --upgrade markovify spacy nltk
RUN python -m spacy download en_core_web_sm

CMD /bin/sh entrypoint.sh
