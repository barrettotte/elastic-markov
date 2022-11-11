import logging
import markovify
import os
import random
import sys
import time
from random_username.generate import generate_username

def init_logger():
    log_level = os.environ.get('LOGLEVEL', 'INFO')
    logger = logging.getLogger()
    logger.setLevel(log_level)
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(log_level)
    stdout_handler.setFormatter(log_formatter)
    logger.addHandler(stdout_handler)

    # file_handler = logging.FileHandler('logs/gen.log')
    # file_handler.setLevel(level=log_level)
    # file_handler.setFormatter(log_formatter)
    # logger.addHandler(file_handler)
    return logger

def generate_ipv4():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def generate_log():
    return '{} {} {}'.format(generate_username(1)[0], generate_ipv4(), model.make_short_sentence(max_chars=128))

logger = init_logger()

with open('data/corpus.txt', 'r') as f:
    corpus = f.readlines()
with open('data/model.json', 'r') as f:
    model = markovify.Text(corpus, state_size=3).from_json(f.read())

while True:
    logger.info(generate_log())
    time.sleep(random.randint(1, 3))
