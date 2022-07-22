from spacy.language import Language
from spacy.tokens import Doc


@Language.component("sub_text")
def create_subtexts(doc):
    # restore「,」index list
    punct_idxs = [0]
    subtexts = []
    for token in doc:
        if token.is_punct:
            punctype = token.morph.get("PunctType")
            punctype = "".join(punctype)
            if punctype == "Comm":
                punct_idxs.append(token.i + 1)
                subtexts.append(doc[punct_idxs[-2]:  punct_idxs[-1]])
    if subtexts:
        Doc.set_extension("sub_texts", default=subtexts, force=True)
    return doc
