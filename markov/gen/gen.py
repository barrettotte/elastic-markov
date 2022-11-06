import markovify
import random
import time

with open('data/corpus.txt', 'r') as f:
    corpus = f.readlines()
with open('data/model.json', 'r') as f:
    model = markovify.Text(corpus, state_size=3).from_json(f.read())

while True:
    
    for i in range(5):
        username = 'username' # TODO:
        sentence = model.make_short_sentence(max_chars=128)
        geo = None # TODO:
        print(sentence)
        # time.sleep(random.randint(1, 3))
    break # TODO:
