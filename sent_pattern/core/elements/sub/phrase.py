from typing import List, Optional
from spacy.tokens import Span, Token, SpanGroup, Doc

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

    def __init__(self, doc:Doc):
        def is_prep(token): return token.text in PhraseData.PREP_LIST
        Token.set_extension("is_prep", getter=is_prep, force=True)
        self._doc = doc
        self.__prep_phrase = self._get_prep_phrase()
    
    @property
    def prep_phrase(self) -> Optional[List[Span]]:
        return self.__prep_phrase
    
    def _get_prep_phrase(self) -> Optional[List[Span]]:
        """method to extract a noun including prep 

        Args:
            doc (Doc): spacy.tokens.Doc class

        Returns:
            Optional[List[Span]]: return a noun including prep 
        """        
        prep_noun = "prep_noun"
        spans = []
        for token in self._doc:
            subs = [sub for sub in token.subtree]
            if token.dep_ == "prep":
                start = subs[0].i
                end = subs[-1].i+1
                span = Span(self._doc, start, end, label=prep_noun)
                spans.append(span)
        return spans