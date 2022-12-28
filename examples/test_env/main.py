import spacy
nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("sent_pattern")
doc = nlp("The Eureka client handles all aspects of service instance registration and deregistration")
get_ext_tuple  = doc.get_extension("sentpattern")
pattern = doc._.sentpattern
print(doc._.sentpattern.subject.root.text)