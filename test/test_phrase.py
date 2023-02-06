from sent_pattern.core.elements.elements import make_custom_elements
from sent_pattern.core.elements.sub.phrase import PrepPhrase
import spacy
from sent_pattern import tags


nlp = spacy.load("en_core_web_lg")

def test_custom_phrase():
    text = "The Eureka client handles all aspects of service instance registration and deregistration"
    doc = nlp(text)
    dep_list = tags.create_dep_list(doc)
    custom = make_custom_elements(doc,dep_list ,opt="prep")
    assert custom.prep.__class__ == PrepPhrase
    

def test_custom_relcl(): 
    text = "The Eureka client handles all aspects of service instance registration and deregistration"
    doc = nlp(text)
    dep_list = tags.create_dep_list(doc)
    custom = make_custom_elements(doc,dep_list ,opt="relcl")
    print(custom.relcl)
    assert custom.relcl == None
