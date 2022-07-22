from spacy.language import Language
from spacy.tokens import Doc


@Language.component("span_noun")
def create_span_noun(doc: Doc):
    """
    process noun_chunks as a single noun
    """
    noun_list = list(doc.noun_chunks)
    with doc.retokenize() as retokenizer:
        for span in noun_list:
            retokenizer.merge(span)
    return doc
