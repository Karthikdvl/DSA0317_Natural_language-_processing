import nltk
from nltk import CFG

cfg_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | V NP PP | V
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'telescope' | 'park'
    V -> 'saw' | 'walked'
    P -> 'in' | 'with'
""")

rd_parser = nltk.RecursiveDescentParser(cfg_grammar)

sentence = "I saw the dog in the park".split()

print("Parsing the sentence:")
for tree in rd_parser.parse(sentence):
    print(tree)
    tree.draw()  
