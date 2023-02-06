from typing import List, Union
from sent_pattern.core.elements.patterns import SentencePatternDoc
from sent_pattern.core.interface.Ipattern import IBaseSentencePattern
from sent_pattern.tags import create_dep_list, create_elements
from spacy.tokens import Doc
from spacy.language import Language


def get_sentpattern_type(doc: Doc)-> Union[IBaseSentencePattern,List[IBaseSentencePattern]]:
    pattern_docs = []
    if len(list(doc.sents)) > 1:
        for d in doc.sents:
            dep_list = create_dep_list(d)
            elements = create_elements(dep_list)
            pattern_doc = SentencePatternDoc(elements)
            pattern_docs.append(pattern_doc.type)
        return pattern_docs
    else:
        dep_list = create_dep_list(doc)
        elements = create_elements(dep_list)
        pattern_doc = SentencePatternDoc(elements)
    return pattern_doc.type

@Language.component("sent_pattern")
def create_sentence_pattern(doc: Doc):
    if not Doc.has_extension("sentpattern"):
        Doc.set_extension("sentpattern", getter=get_sentpattern_type)
    return doc
