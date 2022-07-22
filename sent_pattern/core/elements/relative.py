from spacy.tokens import Doc, Span


class Relative():
    def __init__(self, doc: Doc) -> None:
        self._doc = doc
        self.root = self._get_relative(doc)

    def _get_relative(self, doc: Doc):
        spans = []
        for token in doc:
            if token.dep_ == "relcl":
                subtree = [t for t in token.subtree]
                start = doc[subtree[0].i].i
                end = doc[subtree[-1].i].i+1
                span = Span(doc, start, end, label="relcl")
                spans.append(span)
        return spans
