import spacy
nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("sent_pattern")
doc = nlp("I like yuo")
print(doc._.sentpattern.subject.root.text)
