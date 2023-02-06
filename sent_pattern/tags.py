from collections import defaultdict
from spacy.tokens import Doc
from sent_pattern.core.elements.elements import RootElements, make_root_elements
from sent_pattern.core.elements.patterns import SentencePatternDoc
from sent_pattern.core.type import DepLemmaListType


def create_dep_list(doc: Doc) -> DepLemmaListType:
    """
    Put into dict for each dep of Token
    Parameters
    ----------
    doc: spacy.tokens.Doc
        doc after nlp initialization

    Returns
    -------
    dep_list: Dict[str, Optional[Token]]
    """
    dep_list = defaultdict(list)
    for token in doc:
        dep_list[token.dep_].append(token)
    return dict(dep_list)


def create_elements(dep_list: DepLemmaListType) -> RootElements:
    """
    Parameters
    ----------
    dep_list : DepLemmaListType
        Put into dict for each dep of Token

    Returns
    -------
    elements: RootElements
        classes have subject, verb, adjective, and object
    """
    elements = make_root_elements(
        dep_list=dep_list)
    return elements


def create_sent_pattern(elements: RootElements) -> SentencePatternDoc:
    """
    Parameters
    ----------
    elements : RootElements
        classes have subject, verb, adjective, and object

    Returns
    -------
    pattern : SentencePatternFactory
    """
    pattern = SentencePatternDoc(elements)
    return pattern
