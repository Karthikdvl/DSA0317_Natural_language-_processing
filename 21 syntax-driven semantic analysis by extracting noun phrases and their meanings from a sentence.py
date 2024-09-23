import spacy
nlp = spacy.load("en_core_web_sm")
def extract_noun_phrases(sentence):
    doc = nlp(sentence)
    noun_phrases = []
    for chunk in doc.noun_chunks:
        noun_phrases.append((chunk.text, chunk.root.dep_))
    return noun_phrases
sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases = extract_noun_phrases(sentence)
print("Noun Phrases and their Syntactic Roles:")
for phrase, dep in noun_phrases:
    print(f"'{phrase}' -> {dep}")
