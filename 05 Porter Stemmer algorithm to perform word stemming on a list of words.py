import nltk
from nltk.stem import PorterStemmer
#nltk.download('punkt')
stemmer = PorterStemmer()
words = ["running", "jumps", "easily", "fairly", "leaving", "children", "cats", "studies"]
stemmed_words = [stemmer.stem(word) for word in words]
for word, stemmed_word in zip(words, stemmed_words):
    print(f"Original: {word}, Stemmed: {stemmed_word}")
