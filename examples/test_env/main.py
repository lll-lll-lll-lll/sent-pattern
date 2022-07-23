import spacy
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("sent_pattern")
doc = nlp("I like yuo")
pattern = doc._.sentpattern
print(doc._.sentpattern.subject.root.text)
print(pattern.abbreviation)
