import spacy
nlp = spacy.load('en_core_web_md')
def evaluate_coherence(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    coherence_score = 0
    for i in range(len(sentences) - 1):
        coherence_score += sentences[i].similarity(sentences[i + 1])
    return coherence_score / (len(sentences) - 1)
text = "The weather is nice today. I will go for a walk. The park is nearby."
coherence_score = evaluate_coherence(text)
print("Coherence Score:", coherence_score)

#python -m spacy download en_core_web_md
