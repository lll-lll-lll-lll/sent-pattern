from sent_pattern.core.elements.phrase import PrepPhrase
import spacy
from sent_pattern import tags

from sent_pattern.core.elementsfactory import CustomElements, ElementsFactory

nlp = spacy.load("en_core_web_md")

def test_phrase():
    doc = nlp("The Eureka client handles all aspects of service instance registration and deregistration")
    phrase = PrepPhrase()
    doc = phrase.register_prep_phrase(doc)
    print(doc.spans["prep_noun"])


def test_custom_phrase():
    text = "The Eureka client handles all aspects of service instance registration and deregistration"
    doc = nlp(text)
    dep_list = tags.create_dep_list(doc)
    lemma_list = tags.create_lemma_list(doc)
    custom = ElementsFactory.make_custom_elements(dep_list, lemma_list, doc=doc, option="prep")
    phrase = custom.option
    print(phrase.prep_groups)