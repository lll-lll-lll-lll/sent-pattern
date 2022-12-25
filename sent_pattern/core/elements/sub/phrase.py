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

    def __init__(self):
        def is_prep(token): return token.text in PhraseData.PREP_LIST
        Token.set_extension("is_prep", getter=is_prep, force=True)
    
    @property
    def prep_groups(self):
        return self._span_group

    def register_prep_phrase(self, doc: Doc) -> Doc:
        """
        Add noun including prep to Spans Group
        Parameters
        ----------
        doc : Doc

        Returns
        -------
        doc : Doc
        """
        prep_noun = "prep_noun"
        spans = []
        for token in doc:
            subs = [sub for sub in token.subtree]
            if token.dep_ == "prep":
                start = subs[0].i
                end = subs[-1].i+1
                span = Span(doc, start, end, label=prep_noun)
                spans.append(span)

        self._span_group = SpanGroup(doc=doc, name=prep_noun, spans=spans, attrs={})
        doc.spans[prep_noun] = self._span_group
        return doc