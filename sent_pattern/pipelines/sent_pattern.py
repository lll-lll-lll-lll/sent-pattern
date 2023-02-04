from typing import List, Union
from sent_pattern.core.factory.pattern import SentencePatternDoc
from sent_pattern.core.interface.Ipattern import IBaseSentencePattern
from sent_pattern.tags import create_dep_list, create_elements
from spacy.tokens import Doc
from spacy.language import Language


def get_sentpattern_type(doc: Doc)-> Union[IBaseSentencePattern,List[IBaseSentencePattern]]:
    factories = []
    if len(list(doc.sents)) > 1:
        for d in doc.sents:
            dep_list = create_dep_list(d)
            elements = create_elements(dep_list)
            factory = SentencePatternDoc(elements)
            factories.append(factory)
        return factories
    else:
        dep_list = create_dep_list(doc)
        elements = create_elements(dep_list)
        factory = SentencePatternDoc(elements)
    return factory.pattern_type

@Language.component("sent_pattern")
def create_sentence_pattern(doc: Doc):
    if not Doc.has_extension("sentpattern"):
        Doc.set_extension("sentpattern", getter=get_sentpattern_type)
    return doc
