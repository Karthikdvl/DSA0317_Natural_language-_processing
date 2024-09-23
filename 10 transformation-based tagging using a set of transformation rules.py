import nltk
from nltk.tag import DefaultTagger, UnigramTagger, brill, brill_trainer
nltk.download('treebank')
nltk.download('universal_tagset')
tagged_sentences = nltk.corpus.treebank.tagged_sents(tagset='universal')
default_tagger = DefaultTagger('NOUN')
unigram_tagger = UnigramTagger(tagged_sentences, backoff=default_tagger)
def build_templates():
    templates = [
        brill.Template(brill.Pos([-1])),             
        brill.Template(brill.Pos([1])),              
        brill.Template(brill.Pos([-1]), brill.Pos([1])),  
        brill.Template(brill.Word([-1])),            
        brill.Template(brill.Word([1])),             
    ]
    return templates
templates = build_templates()
brill_trainer_instance = brill_trainer.BrillTaggerTrainer(initial_tagger=unigram_tagger, templates=templates, trace=3)
brill_tagger = brill_trainer_instance.train(tagged_sentences)
test_sentence = "The cat is chasing the mice".split()
brill_tags = brill_tagger.tag(test_sentence)
print(brill_tags)
