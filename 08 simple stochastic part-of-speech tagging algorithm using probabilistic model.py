import nltk
from collections import defaultdict

#nltk.download('treebank')
#nltk.download('universal_tagset')

tagged_sentences = nltk.corpus.treebank.tagged_sents(tagset='universal')

word_tag_freq = defaultdict(lambda: defaultdict(int))

for sentence in tagged_sentences:
    for word, tag in sentence:
        word_tag_freq[word.lower()][tag] += 1
        
def predict_pos(word):
    word = word.lower()
    if word in word_tag_freq:
        
        return max(word_tag_freq[word], key=word_tag_freq[word].get)
    else:
       
        return 'NOUN'

def tag_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    return [(word, predict_pos(word)) for word in words]

sentence = "The quick brown fox jumps over the lazy dog."
tagged_sentence = tag_sentence(sentence)

print("Tagged Sentence:")
print(tagged_sentence)
