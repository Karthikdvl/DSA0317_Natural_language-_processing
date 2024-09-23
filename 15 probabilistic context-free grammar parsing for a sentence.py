import nltk
from nltk import PCFG
grammar = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> Det N [0.6] | 'dogs' [0.4]
  VP -> V NP [1.0]
  Det -> 'the' [1.0]
  N -> 'cat' [0.5] | 'dog' [0.5]
  V -> 'chases' [1.0]
""")
sentence = ['the', 'cat', 'chases', 'dogs']
parser = nltk.ViterbiParser(grammar)
for tree in parser.parse(sentence):
    tree.pretty_print()
    tree.draw()
