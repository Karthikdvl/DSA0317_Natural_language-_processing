import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

sentence = "The cats are playing with the balls. They played joyfully"

words = word_tokenize(sentence)

print("Stemming Results:")
for word in words:
    print(f"{word} -> {stemmer.stem(word)}")

print("\nLemmatization Results:")
for word in words:
    print(f"{word} -> {lemmatizer.lemmatize(word)}")
