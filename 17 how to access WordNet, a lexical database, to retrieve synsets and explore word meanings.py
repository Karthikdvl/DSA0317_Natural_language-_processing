import nltk
from nltk.corpus import wordnet as wn
#nltk.download('wordnet')
synsets = wn.synsets('bank')
for synset in synsets:
    print(f"Synset: {synset.name()}, Definition: {synset.definition()}")
