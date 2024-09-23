import nltk
from nltk import CFG
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V_sg | V_pl
  Det -> 'the'
  N -> 'cat' | 'dogs'
  V_sg -> 'chases'
  V_pl -> 'chase'
""")
sentence = ['the', 'cat', 'chases']  
parser = nltk.ChartParser(grammar)
valid = False
for tree in parser.parse(sentence):
    tree.pretty_print()
    tree.draw()
    valid = True
if not valid:
    print("Invalid sentence: Subject-verb agreement failed.")
