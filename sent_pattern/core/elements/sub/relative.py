from typing import List, Optional
from spacy.tokens import Doc, Span


class RelativeClause():
    def __init__(self, doc: Doc) -> None:
        self._doc = doc
        self.relcl_section = self._get_relative(doc)

    def _get_relative(self, doc: Doc) -> Optional[List[Span]]:
        """method to extract relational clauses from Doc class and return them as a list

        Args:
            doc (Doc): spacy.tokens.Doc class

        Returns:
            Optional[List[Span]]: return spacy.tokens.Span list
        """        
        spans = []
        for token in doc:
            if token.dep_ == "relcl":
                subtree = [t for t in token.subtree]
                start = doc[subtree[0].i].i
                end = doc[subtree[-1].i].i+1
                span = Span(doc, start, end, label="relcl")
                spans.append(span)
        return spans
