import logging
import markovify
import os
import random
import sys
import time
from random_username.generate import generate_username

logging.basicConfig(stream=sys.stdout, level=os.environ.get('LOGLEVEL', 'INFO'), format='%(asctime)s %(levelname)s %(message)s')

def generate_ipv4():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def generate_log():
    return '{} {} {}'.format(generate_username(1)[0], generate_ipv4(), model.make_short_sentence(max_chars=128))

with open('data/corpus.txt', 'r') as f:
    corpus = f.readlines()
with open('data/model.json', 'r') as f:
    model = markovify.Text(corpus, state_size=3).from_json(f.read())

while True:
    logging.info(generate_log())
    time.sleep(random.randint(1, 3))
