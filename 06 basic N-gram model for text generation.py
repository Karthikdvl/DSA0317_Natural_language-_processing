import random
import nltk
from collections import defaultdict

sample_text = """Artificial intelligence is transforming industries. 
Machines are learning to perform tasks that traditionally required human intelligence. 
As technology evolves, AI systems are becoming more efficient, autonomous, and intelligent."""

#nltk.download('punkt')
words = nltk.word_tokenize(sample_text.lower())

bigram_model = defaultdict(list)

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    bigram_model[word].append(next_word)

def generate_text(start_word, length=20):
    current_word = start_word
    output = [current_word]
    
    for _ in range(length - 1):
        next_words = bigram_model.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        output.append(current_word)
    
    return ' '.join(output)

start_word = 'artificial'  
generated_text = generate_text(start_word, length=20)

print("Generated Text:")
print(generated_text)
