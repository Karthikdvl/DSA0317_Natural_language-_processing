import nltk
from nltk import RegexpTagger
from nltk.corpus import treebank
#nltk.download('treebank')
#nltk.download('universal_tagset')
sentences = treebank.sents()
patterns = [
    (r'^[Tt]he$', 'DET'),           
    (r'^[Aa]n?$', 'DET'),            
    (r'.*ing$', 'VERB'),             
    (r'.*ed$', 'VERB'),             
    (r'.*es$', 'VERB'),              
    (r'.*ould$', 'VERB'),            
    (r'.*\'s$', 'NOUN'),             
    (r'.*s$', 'NOUN'),              
    (r'^[A-Z].*$', 'NOUN'),          
    (r'\b[0-9]+\b', 'NUM'),         
    (r'.*', 'NOUN')                  
]
regexp_tagger = RegexpTagger(patterns)
test_sentence = ["The", "cat", "is", "chasing", "the", "mice"]
tags = regexp_tagger.tag(test_sentence)
print(tags)
