from nltk.wsd import lesk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import nltk
#nltk.download('wordnet')
#nltk.download('punkt')
sentence = "I went to the bank to deposit money."
tokens = word_tokenize(sentence)
sense = lesk(tokens, 'bank')
print(f"Sense: {sense}, Definition: {sense.definition()}")
