import spacy
from sent_pattern import tags
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("sent_pattern")
doc = nlp("I like you")
dep_list = tags.create_dep_list(doc)
elements  = tags.create_elements(dep_list=dep_list)
p  = tags.create_sent_pattern(elements=elements)
print(p.pattern_type)