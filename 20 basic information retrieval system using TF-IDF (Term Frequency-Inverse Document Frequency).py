from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "The cat sat on the mat",
    "The dog barked loudly",
    "The sun shines brightly"
]
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
feature_names = tfidf_vectorizer.get_feature_names_out()
for doc_idx, doc in enumerate(tfidf_matrix):
    print(f"Document {doc_idx + 1}")
    for word_idx in doc.nonzero()[1]:
        print(f"Word: {feature_names[word_idx]}, Score: {doc[0, word_idx]}")
