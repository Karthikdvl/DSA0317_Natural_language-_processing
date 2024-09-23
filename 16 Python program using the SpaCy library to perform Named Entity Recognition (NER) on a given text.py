import spacy
nlp = spacy.load('en_core_web_sm')

text = "Apple is looking at buying U.K. startup for $1 billion"
doc = nlp(text)

for token in doc:
    print(token.text, token.pos_)
