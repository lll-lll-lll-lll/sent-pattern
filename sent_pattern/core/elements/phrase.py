from spacy.tokens import Span, Token, SpanGroup, Doc
from typing import List


class PhraseData:
    PREP_LIST = [
        "about", "after", "as", "at", "before", "by", "for", "from", "in", "into", "near", "of", "on", "over", "to",
        "under", "with", "above", "across", "against", "along", "among", "around", "behind", "below", "beside",
        "between", "despite", " during", "except", " like", "off", "onto", "since", "than", "throughout", "toward",
        "toward", "until", "via", "within", "without", "worth", "anti", "beneath", " beyond", " concering", "down",
        "excluding", "including", "inside", "outside", "past", "per", "pro", "regarding", "underneath", "unlike", "up",
        "versus", "aboard", "alongside", "amid", "but", "circa", "failing", "fllowing", "minus", "opposite", "out", "plus",
        "times", "abaft", "absent", "apropos", "astride", "athwart", "given", "next", "pace", "qua", "save",
    ]


class PrepPhrase():

    def __init__(self, doc: Doc):
        def is_prep(token): return token.text in PhraseData.PREP_LIST
        Token.set_extension("is_prep", getter=is_prep, force=True)
        return doc

    def register_prep_phrase(self, doc: Doc) -> Doc:
        spans = []
        for token in doc:
            subs = [sub for sub in token.subtree]
            if token.dep_ == "prep":
                start = subs[0].i
                end = subs[-1].i+1
                span = Span(doc, start, end, label="prep_noun")
                spans.append(span)

        doc = self._create_spangroup(doc, "prep_noun", spans)
        return doc

    def _create_spangroup(self, doc: Doc, prep_name: str, spans: List[Span], attrs={}) -> Doc:
        span_group = SpanGroup(doc=doc, name=prep_name, spans=spans, attrs=attrs)
        doc.spans[prep_name] = span_group
        return doc
