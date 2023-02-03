from sent_pattern.core.factory.pattern import SentencePattern
from sent_pattern.core.interface.Ipattern import IBaseSentencePattern
from sent_pattern.tags import create_dep_list, create_elements
from spacy.tokens import Doc
from spacy.language import Language


def get_sentpattern_type(doc: Doc)-> IBaseSentencePattern:
    dep_list = create_dep_list(doc)
    elements = create_elements(dep_list)
    factory = SentencePattern(elements)
    return factory.pattern_type

@Language.component("sent_pattern")
def create_sentence_pattern(doc: Doc):
    if not Doc.has_extension("sentpattern"):
        Doc.set_extension("sentpattern", getter=get_sentpattern_type)
    return doc
