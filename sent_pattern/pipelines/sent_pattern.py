from sent_pattern.core.patternfactory import PatternFactory
from sent_pattern.tags import create_dep_list, create_lemma_list, create_elements
from spacy.tokens import Doc
from spacy.language import Language


@Language.component("sent_pattern")
def create_sentence_pattern(doc: Doc):
    dep_list = create_dep_list(doc)
    lemma_list = create_lemma_list(doc)
    elements = create_elements(dep_list, lemma_list)
    factory = PatternFactory(elements)
    if not Doc.has_extension("sentpattern"):
        Doc.set_extension("sentpattern", default=None)
    doc._.sentpattern = factory.pattern_type
    return doc
