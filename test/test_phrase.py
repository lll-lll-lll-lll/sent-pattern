from sent_pattern.core.elements.sub.phrase import PrepPhrase
import spacy
from sent_pattern import tags

from sent_pattern.core.factory.elements import  ElementsFactory

nlp = spacy.load("en_core_web_lg")

def test_phrase():
    doc = nlp("The Eureka client handles all aspects of service instance registration and deregistration")
    phrase = PrepPhrase()
    doc = phrase.prep_phrase(doc)
    print(doc.spans["prep_noun"])


def test_custom_phrase():
    text = "The Eureka client handles all aspects of service instance registration and deregistration"
    doc = nlp(text)
    dep_list = tags.create_dep_list(doc)
    custom = ElementsFactory.make_custom_elements(dep_list, doc=doc, opt="prep")
    phrase = custom.option