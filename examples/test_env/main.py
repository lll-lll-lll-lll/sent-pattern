import spacy
from sent_pattern import tags
nlp = spacy.load("en_core_web_sm")
doc = nlp("he makes me happy")
dep_list = tags.create_dep_list(doc)
elements  = tags.create_elements(dep_list=dep_list)
p  = tags.create_sent_pattern(elements=elements)
pattern = p.type
print(pattern.subject.root.text)
# he (string)
print(pattern.verb.root)
# gives(spacy.Token)
print(dep_list)
# {'ROOT': [gives], 'dative': [me], 'dobj': [something], 'nsubj': [he]}
print(pattern.abbreviation)
# SVO (str)