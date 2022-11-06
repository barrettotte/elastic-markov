import markovify
import nltk
import os
import re
import spacy

CORPUS_PATH = './data/corpus.txt'
MODEL_PATH = './data/model.json'

if os.path.isfile(CORPUS_PATH) and os.path.isfile(MODEL_PATH):
    print('Model already trained.')
    exit(0) # already trained

nltk.download('gutenberg')
nlp = spacy.load('en_core_web_sm') # python3 -m spacy download en_core_web_sm
nlp.max_length = 1500000

def clean(corpus):
    corpus = re.sub(r'CHAPTER \d+', '', corpus)
    corpus = re.sub(r'--', ' ', corpus)
    corpus = re.sub('[\[].*?[\]]', '', corpus)
    corpus = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', corpus)
    corpus = corpus.replace('\n', '').replace('\t', '')
    corpus = ' '.join(corpus.split())
    return corpus

corpus = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
corpus = clean(corpus[corpus.find('CHAPTER 1'):])
corpus = [s.text for s in nlp(corpus).sents if len(s.text) > 1]

with open(CORPUS_PATH, 'w+') as f:
    f.write('\n'.join(corpus))

model = markovify.Text(' '.join(corpus), state_size=3).compile()

with open(MODEL_PATH, 'w+') as f:
    f.write(model.to_json())
