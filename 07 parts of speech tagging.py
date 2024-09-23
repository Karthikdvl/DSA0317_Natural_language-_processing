import nltk
from nltk import word_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
text = """The quick brown fox jumps over the lazy dog. Artificial Intelligence is transforming the world rapidly."""
tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
for word, tag in pos_tags:
    print(f'{word}: {tag}')
