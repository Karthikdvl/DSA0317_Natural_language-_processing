import spacy
import neuralcoref
nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)
def resolve_references(text):
    doc = nlp(text)
    return doc._.coref_resolved
text = "John loves his dog. He takes it out for walks every day."
resolved_text = resolve_references(text)
print("Resolved Text:", resolved_text)

#python -m spacy download en_core_web_sm
